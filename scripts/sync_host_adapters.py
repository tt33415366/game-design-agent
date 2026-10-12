#!/usr/bin/env python3
"""Render checked-in host adapter projections from canonical project sources."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
import tomllib
from pathlib import Path, PurePosixPath
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = PurePosixPath("agents/generated-host-files.json")
ROLE_NAMES = ("explorer", "researcher", "reviewer", "tester", "worker")
SKILL_NAMES = (
    "design-intake",
    "gameplay-design",
    "system-design",
    "design-prototype",
    "design-review",
    "design-change",
)
REQUIRED_SKILL_FILES = {
    "design-intake": {"SKILL.md", "templates/design-brief.md"},
    "gameplay-design": {"SKILL.md", "templates/gameplay-proposal.md"},
    "system-design": {"SKILL.md", "templates/system-specification.md"},
    "design-prototype": {"SKILL.md", "templates/evidence-log.md", "templates/validation-plan.md"},
    "design-review": {"SKILL.md", "templates/design-review.md", "templates/development-handoff.md"},
    "design-change": {"SKILL.md", "templates/change-history.md", "templates/change-impact.md"},
}
CLAUDE_TOOLS = frozenset(
    {"Read", "Glob", "Grep", "WebSearch", "WebFetch", "Edit", "Write", "Bash"}
)
ANTIGRAVITY_TOOLS = frozenset(
    {
        "view_file",
        "list_dir",
        "find_by_name",
        "grep_search",
        "search_web",
        "read_url_content",
        "write_to_file",
        "replace_file_content",
        "multi_replace_file_content",
        "run_command",
        "manage_task",
    }
)
CLAUDE_NATIVE_DELEGATION_TOOLS = frozenset({"Agent"})
ANTIGRAVITY_NATIVE_DELEGATION_TOOLS = frozenset(
    {"invoke_subagent", "define_subagent", "send_message", "manage_subagents"}
)


class AdapterError(Exception):
    pass


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def relative_path(value: str | PurePosixPath) -> PurePosixPath:
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or path == PurePosixPath("."):
        raise AdapterError(f"unsafe managed path: {value}")
    return path


def is_managed_path(path: PurePosixPath) -> bool:
    parts = path.parts
    return (
        len(parts) == 3
        and parts[:2] == (".claude", "agents")
        and parts[2] in {f"{role}.md" for role in ROLE_NAMES}
    ) or (
        len(parts) >= 4
        and parts[:2] == (".claude", "skills")
        and parts[2] in SKILL_NAMES
    ) or (
        len(parts) == 3
        and parts[:2] == (".agents", "agents")
        and parts[2] in {f"{role}.md" for role in ROLE_NAMES}
    )


def checked_path(root: Path, relative: str | PurePosixPath) -> Path:
    path = relative_path(relative)
    current = root
    for index, part in enumerate(path.parts):
        current = current / part
        if current.is_symlink():
            raise AdapterError(f"symlink in managed path: {path}")
        if current.exists() and index < len(path.parts) - 1 and not current.is_dir():
            raise AdapterError(f"non-directory managed path ancestor: {path}")
    try:
        current.resolve(strict=False).relative_to(root.resolve())
    except ValueError as error:
        raise AdapterError(f"managed path escapes repository: {path}") from error
    return current


def yaml_scalar(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def yaml_list(values: list[str]) -> str:
    return "[" + ", ".join(yaml_scalar(value) for value in values) + "]"


def normalized_text(value: str) -> str:
    normalized = value.replace("\r\n", "\n").replace("\r", "\n")
    return normalized if normalized.endswith("\n") else normalized + "\n"


def load_json(path: Path) -> dict[str, object]:
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise AdapterError(f"invalid JSON {path}: {error}") from error
    if not isinstance(parsed, dict):
        raise AdapterError(f"invalid JSON object: {path}")
    return parsed


def load_manifest(root: Path) -> dict[str, str]:
    path = checked_path(root, MANIFEST_PATH)
    if not path.exists():
        return {}
    document = load_json(path)
    files = document.get("files")
    if not isinstance(files, dict) or set(document) != {"files"}:
        raise AdapterError("invalid generated-files manifest")
    result: dict[str, str] = {}
    for relative, digest in files.items():
        if not isinstance(relative, str) or not isinstance(digest, str):
            raise AdapterError("invalid generated-files manifest entry")
        safe = relative_path(relative).as_posix()
        if len(digest) != 64 or any(character not in "0123456789abcdef" for character in digest):
            raise AdapterError(f"invalid digest for {relative}")
        if not is_managed_path(PurePosixPath(safe)):
            raise AdapterError(f"manifest path outside generated host namespace: {relative}")
        result[safe] = digest
    return result


def load_claude_metadata(root: Path) -> dict[str, list[str]]:
    document = load_json(checked_path(root, "agents/host-adapters.json"))
    try:
        roles = document["claude"]
        if not isinstance(roles, dict):
            raise TypeError
        entries = roles["roles"]
        if not isinstance(entries, dict) or set(entries) != set(ROLE_NAMES):
            raise TypeError
    except (KeyError, TypeError) as error:
        raise AdapterError("invalid Claude adapter metadata") from error
    metadata: dict[str, list[str]] = {}
    for role in ROLE_NAMES:
        entry = entries[role]
        if not isinstance(entry, dict) or set(entry) != {"tools"}:
            raise AdapterError(f"invalid Claude metadata for {role}")
        tools = entry["tools"]
        if not isinstance(tools, list) or not all(isinstance(tool, str) for tool in tools):
            raise AdapterError(f"invalid Claude tools for {role}")
        if len(set(tools)) != len(tools) or not set(tools) <= CLAUDE_TOOLS:
            raise AdapterError(f"unsupported Claude tool for {role}")
        if set(tools) & CLAUDE_NATIVE_DELEGATION_TOOLS:
            raise AdapterError(f"native delegation tool for {role}")
        if role in {"explorer", "reviewer"} and set(tools) != {"Read", "Glob", "Grep"}:
            raise AdapterError(f"read-only Claude tools for {role} are invalid")
        if role == "researcher" and set(tools) != {"Read", "Glob", "Grep", "WebSearch", "WebFetch"}:
            raise AdapterError("researcher Claude tools are invalid")
        if role in {"worker", "tester"} and set(tools) != {"Read", "Glob", "Grep", "Edit", "Write", "Bash"}:
            raise AdapterError(f"writer Claude tools for {role} are invalid")
        metadata[role] = tools
    return metadata


def load_antigravity_metadata(root: Path) -> dict[str, list[str]]:
    document = load_json(checked_path(root, "agents/host-adapters.json"))
    try:
        roles = document["antigravity"]
        if not isinstance(roles, dict):
            raise TypeError
        entries = roles["roles"]
        if not isinstance(entries, dict) or set(entries) != set(ROLE_NAMES):
            raise TypeError
    except (KeyError, TypeError) as error:
        raise AdapterError("invalid Antigravity adapter metadata") from error
    metadata: dict[str, list[str]] = {}
    for role in ROLE_NAMES:
        entry = entries[role]
        if not isinstance(entry, dict) or set(entry) != {"tools"}:
            raise AdapterError(f"invalid Antigravity metadata for {role}")
        tools = entry["tools"]
        if not isinstance(tools, list) or not all(isinstance(tool, str) for tool in tools):
            raise AdapterError(f"invalid Antigravity tools for {role}")
        if len(set(tools)) != len(tools) or not set(tools) <= ANTIGRAVITY_TOOLS:
            raise AdapterError(f"unsupported Antigravity tool for {role}")
        if set(tools) & ANTIGRAVITY_NATIVE_DELEGATION_TOOLS:
            raise AdapterError(f"native delegation tool for {role}")
        if role in {"explorer", "reviewer"} and set(tools) != {
            "view_file",
            "list_dir",
            "find_by_name",
            "grep_search",
        }:
            raise AdapterError(f"read-only Antigravity tools for {role} are invalid")
        if role == "researcher" and set(tools) != {
            "view_file",
            "list_dir",
            "find_by_name",
            "grep_search",
            "search_web",
            "read_url_content",
        }:
            raise AdapterError("researcher Antigravity tools are invalid")
        if role in {"worker", "tester"} and set(tools) != {
            "view_file",
            "list_dir",
            "find_by_name",
            "grep_search",
            "write_to_file",
            "replace_file_content",
            "multi_replace_file_content",
            "run_command",
            "manage_task",
        }:
            raise AdapterError(f"writer Antigravity tools for {role} are invalid")
        metadata[role] = tools
    return metadata


def load_canonical_role(root: Path, role: str) -> dict[str, str]:
    source = checked_path(root, f".codex/agents/{role}.toml")
    try:
        with source.open("rb") as file:
            canonical = tomllib.load(file)
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise AdapterError(f"invalid canonical role {role}: {error}") from error
    required = {"name", "description", "developer_instructions"}
    if not required <= set(canonical) or not all(isinstance(canonical[key], str) for key in required):
        raise AdapterError(f"invalid canonical role fields for {role}")
    if canonical["name"] != role:
        raise AdapterError(f"canonical role name mismatch for {role}")
    return {key: canonical[key] for key in required}


def render_claude_role(root: Path, role: str, tools: list[str]) -> bytes:
    canonical = load_canonical_role(root, role)
    frontmatter = "\n".join(
        (
            "---",
            f"name: {yaml_scalar(canonical['name'])}",
            f"description: {yaml_scalar(canonical['description'])}",
            f"tools: {yaml_list(tools)}",
            "model: inherit",
            "permissionMode: default",
            "---",
            "",
        )
    )
    return (frontmatter + normalized_text(canonical["developer_instructions"])).encode("utf-8")


def render_antigravity_role(root: Path, role: str, tools: list[str]) -> bytes:
    canonical = load_canonical_role(root, role)
    frontmatter = "\n".join(
        (
            "---",
            f"name: {yaml_scalar(canonical['name'])}",
            f"description: {yaml_scalar(canonical['description'])}",
            f"tools: {yaml_list(tools)}",
            "model: inherit",
            "subagent: true",
            "mainAgent: false",
            "commandExecutionPolicy: sandbox",
            "---",
            "",
        )
    )
    return (frontmatter + normalized_text(canonical["developer_instructions"])).encode("utf-8")


def render(root: Path) -> dict[str, bytes]:
    claude_metadata = load_claude_metadata(root)
    antigravity_metadata = load_antigravity_metadata(root)
    outputs = {
        f".claude/agents/{role}.md": render_claude_role(root, role, claude_metadata[role])
        for role in ROLE_NAMES
    }
    outputs.update(
        {
            f".agents/agents/{role}.md": render_antigravity_role(root, role, antigravity_metadata[role])
            for role in ROLE_NAMES
        }
    )
    for skill in SKILL_NAMES:
        source_root = checked_path(root, f".agents/skills/{skill}")
        if not source_root.is_dir():
            raise AdapterError(f"missing canonical skill directory: {skill}")
        if source_root.is_symlink():
            raise AdapterError(f"symlinked canonical skill directory: {skill}")
        nodes = list(source_root.rglob("*"))
        if any(path.is_symlink() for path in nodes):
            raise AdapterError(f"symlink in canonical skill tree: {skill}")
        files = [path for path in nodes if path.is_file()]
        relative_files = {source.relative_to(source_root).as_posix() for source in files}
        if not REQUIRED_SKILL_FILES[skill] <= relative_files:
            raise AdapterError(f"missing canonical skill template: {skill}")
        for source in files:
            if source.is_symlink():
                raise AdapterError(f"symlinked canonical skill file: {source.relative_to(root)}")
            target = PurePosixPath(".claude/skills") / skill / source.relative_to(source_root).as_posix()
            outputs[relative_path(target).as_posix()] = source.read_bytes()
    return outputs


def manifest_bytes(outputs: dict[str, bytes]) -> bytes:
    document = {"files": {path: sha256(outputs[path]) for path in sorted(outputs)}}
    return (json.dumps(document, indent=2, sort_keys=True) + "\n").encode("utf-8")


def validate_changes(root: Path, outputs: dict[str, bytes], previous: dict[str, str]) -> tuple[list[str], list[str]]:
    desired = set(outputs)
    prior = set(previous)
    for path in desired | prior | {MANIFEST_PATH.as_posix()}:
        checked_path(root, path)
    for path in sorted(desired):
        destination = checked_path(root, path)
        if not destination.exists():
            continue
        if destination.is_dir():
            raise AdapterError(f"directory at generated file path: {path}")
        actual = destination.read_bytes()
        expected_prior = previous.get(path)
        if expected_prior is None:
            raise AdapterError(f"unmanaged generated-file collision: {path}")
        if sha256(actual) != expected_prior and actual != outputs[path]:
            raise AdapterError(f"locally modified generated file: {path}")
    removals: list[str] = []
    for path in sorted(prior - desired):
        destination = checked_path(root, path)
        if destination.exists():
            if sha256(destination.read_bytes()) != previous[path]:
                raise AdapterError(f"locally modified stale generated file: {path}")
            removals.append(path)
    writes = [path for path in sorted(desired) if not checked_path(root, path).exists() or checked_path(root, path).read_bytes() != outputs[path]]
    return writes, removals


def atomic_replace(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as temporary:
            temporary.write(data)
            temporary.flush()
            os.fsync(temporary.fileno())
        os.replace(temporary_name, path)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise


def apply_changes(
    root: Path,
    outputs: dict[str, bytes],
    previous: dict[str, str],
    replace: Callable[[Path, bytes], None] = atomic_replace,
) -> None:
    writes, removals = validate_changes(root, outputs, previous)
    for path in writes:
        replace(checked_path(root, path), outputs[path])
    for path in removals:
        checked_path(root, path).unlink()
    replace(checked_path(root, MANIFEST_PATH), manifest_bytes(outputs))


def check(root: Path, outputs: dict[str, bytes], previous: dict[str, str]) -> list[str]:
    errors: list[str] = []
    expected = {path: sha256(data) for path, data in outputs.items()}
    if previous != expected:
        errors.append("generated-files manifest does not match expected output")
    for path, data in sorted(outputs.items()):
        destination = checked_path(root, path)
        if not destination.exists():
            errors.append(f"missing generated file: {path}")
        elif destination.read_bytes() != data:
            errors.append(f"generated file differs: {path}")
    for path in sorted(set(previous) - set(outputs)):
        if checked_path(root, path).exists():
            errors.append(f"stale generated file: {path}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    command = parser.add_mutually_exclusive_group(required=True)
    command.add_argument("--write", action="store_true")
    command.add_argument("--check", action="store_true")
    arguments = parser.parse_args(argv)
    try:
        outputs = render(ROOT)
        previous = load_manifest(ROOT)
        if arguments.write:
            apply_changes(ROOT, outputs, previous)
        else:
            errors = check(ROOT, outputs, previous)
            if errors:
                print("\n".join(errors), file=sys.stderr)
                return 1
    except AdapterError as error:
        print(f"host adapter sync failed: {error}", file=sys.stderr)
        return 1
    except OSError as error:
        print(f"host adapter sync failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
