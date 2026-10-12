from __future__ import annotations

import json
import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = REPOSITORY_ROOT / "scripts/sync_host_adapters.py"
ROLES = ("explorer", "researcher", "reviewer", "tester", "worker")
SKILLS = (
    "design-intake",
    "gameplay-design",
    "system-design",
    "design-prototype",
    "design-review",
    "design-change",
)


def fixture_repository() -> tempfile.TemporaryDirectory[str]:
    temporary = tempfile.TemporaryDirectory(prefix="claude adapter ")
    root = Path(temporary.name) / "repository with spaces"
    (root / "scripts").mkdir(parents=True)
    shutil.copy2(SCRIPT, root / "scripts/sync_host_adapters.py")
    (root / "agents").mkdir()
    shutil.copy2(
        REPOSITORY_ROOT / "agents/host-adapters.json",
        root / "agents/host-adapters.json",
    )
    shutil.copytree(REPOSITORY_ROOT / ".codex/agents", root / ".codex/agents")
    shutil.copytree(REPOSITORY_ROOT / ".agents/skills", root / ".agents/skills")
    return temporary


def run_renderer(root: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(root / "scripts/sync_host_adapters.py"), *arguments],
        cwd=Path.cwd(),
        capture_output=True,
        text=True,
        check=False,
    )


def load_renderer(root: Path):
    specification = importlib.util.spec_from_file_location("adapter_sync", root / "scripts/sync_host_adapters.py")
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


class AdapterSyncTests(unittest.TestCase):
    def test_normalized_text_preserves_trailing_newlines(self) -> None:
        renderer = load_renderer(REPOSITORY_ROOT)

        self.assertEqual("body\n\n", renderer.normalized_text("body\r\n\r\n"))
        self.assertEqual("body\n\n\n", renderer.normalized_text("body\r\r\r"))
        self.assertEqual("body\n", renderer.normalized_text("body\r\n"))
        self.assertEqual("body\n", renderer.normalized_text("body"))

    def test_six_skill_trees_match(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            result = run_renderer(root, "--write")

            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            manifest = json.loads((root / "agents/generated-host-files.json").read_text())
            managed_paths = set(manifest["files"])
            self.assertEqual(
                {f".claude/agents/{role}.md" for role in ROLES}
                | {f".agents/agents/{role}.md" for role in ROLES}
                | {
                    (Path(".claude/skills") / skill / path.relative_to(root / ".agents/skills" / skill)).as_posix()
                    for skill in SKILLS
                    for path in (root / ".agents/skills" / skill).rglob("*")
                    if path.is_file()
                },
                managed_paths,
            )
            for role in ROLES:
                content = (root / f".claude/agents/{role}.md").read_text()
                self.assertIn(f'name: "{role}"', content)
                self.assertIn("model: inherit", content)
                self.assertIn("permissionMode: default", content)

            for skill in SKILLS:
                source = root / ".agents/skills" / skill
                destination = root / ".claude/skills" / skill
                self.assertTrue(destination.is_dir())
                self.assertEqual(
                    {
                        file.relative_to(source): file.read_bytes()
                        for file in source.rglob("*")
                        if file.is_file()
                    },
                    {
                        file.relative_to(destination): file.read_bytes()
                        for file in destination.rglob("*")
                        if file.is_file()
                    },
                )

    def write_fixture(self, root: Path) -> None:
        result = run_renderer(root, "--write")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_role_body_matches_source(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            self.write_fixture(root)
            for role in ROLES:
                source = (root / f".codex/agents/{role}.toml").read_text()
                expected_body = source.split('developer_instructions = """', 1)[1].rsplit('"""', 1)[0]
                actual = (root / f".claude/agents/{role}.md").read_text().split("---\n", 2)[2]
                self.assertEqual(expected_body.lstrip("\n").replace("\r\n", "\n"), actual)

    def test_host_fields_do_not_leak(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            self.write_fixture(root)
            for role in ROLES:
                frontmatter = (root / f".claude/agents/{role}.md").read_text().split("---", 2)[1]
                self.assertIn("model: inherit", frontmatter)
                self.assertIn("permissionMode: default", frontmatter)
                self.assertNotIn("model_reasoning_effort", frontmatter)
                self.assertNotIn("sandbox_mode", frontmatter)

    def test_read_only_tools(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            self.write_fixture(root)
            expected = {
                "explorer": '["Read", "Glob", "Grep"]',
                "reviewer": '["Read", "Glob", "Grep"]',
                "researcher": '["Read", "Glob", "Grep", "WebSearch", "WebFetch"]',
                "worker": '["Read", "Glob", "Grep", "Edit", "Write", "Bash"]',
                "tester": '["Read", "Glob", "Grep", "Edit", "Write", "Bash"]',
            }
            for role, tools in expected.items():
                content = (root / f".claude/agents/{role}.md").read_text()
                self.assertIn(f"tools: {tools}", content)

    def test_all_roles_exclude_native_delegation(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            self.write_fixture(root)
            for role in ROLES:
                content = (root / f".claude/agents/{role}.md").read_text()
                self.assertNotIn("Agent", content)

    def test_repeat_write_is_identical_and_check_does_not_write(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            self.write_fixture(root)
            before = {
                path.relative_to(root): path.read_bytes()
                for path in (root / ".claude").rglob("*")
                if path.is_file()
            }
            before[Path("agents/generated-host-files.json")] = (
                root / "agents/generated-host-files.json"
            ).read_bytes()
            self.assertEqual(0, run_renderer(root, "--check").returncode)
            self.assertEqual(0, run_renderer(root, "--write").returncode)
            after = {
                path.relative_to(root): path.read_bytes()
                for path in (root / ".claude").rglob("*")
                if path.is_file()
            }
            after[Path("agents/generated-host-files.json")] = (
                root / "agents/generated-host-files.json"
            ).read_bytes()
            self.assertEqual(before, after)

    def test_changed_generated_file_is_preserved(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            self.write_fixture(root)
            changed = root / ".claude/agents/explorer.md"
            changed.write_text("local edit\n")
            result = run_renderer(root, "--write")
            self.assertNotEqual(0, result.returncode)
            self.assertIn("locally modified", result.stderr)
            self.assertEqual("local edit\n", changed.read_text())

    def test_unmanaged_collision_is_preserved(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            collision = root / ".claude/agents/explorer.md"
            collision.parent.mkdir(parents=True)
            collision.write_text("local file\n")
            result = run_renderer(root, "--write")
            self.assertNotEqual(0, result.returncode)
            self.assertIn("unmanaged generated-file collision", result.stderr)
            self.assertEqual("local file\n", collision.read_text())
            self.assertFalse((root / "agents/generated-host-files.json").exists())

    def test_stale_output_cleanup(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            self.write_fixture(root)
            manifest_path = root / "agents/generated-host-files.json"
            manifest = json.loads(manifest_path.read_text())
            stale = root / ".claude/skills/design-intake/obsolete.md"
            stale.write_text("obsolete\n")
            manifest["files"][".claude/skills/design-intake/obsolete.md"] = __import__("hashlib").sha256(
                stale.read_bytes()
            ).hexdigest()
            manifest_path.write_text(json.dumps(manifest))
            result = run_renderer(root, "--write")
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertFalse(stale.exists())

    def test_rejects_symlink_escape(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            destination = root / ".claude"
            destination.symlink_to(root / "outside", target_is_directory=True)
            result = run_renderer(root, "--write")
            self.assertNotEqual(0, result.returncode)
            self.assertIn("symlink", result.stderr)
            self.assertFalse((root / "agents/generated-host-files.json").exists())

    def test_invalid_inputs_write_nothing(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            (root / "agents/host-adapters.json").write_text("{bad json")
            result = run_renderer(root, "--write")
            self.assertNotEqual(0, result.returncode)
            self.assertFalse((root / ".claude").exists())
            self.assertFalse((root / "agents/generated-host-files.json").exists())

    def test_malformed_toml_and_missing_skill_template_write_nothing(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            (root / ".codex/agents/explorer.toml").write_text("not = [valid")
            malformed = run_renderer(root, "--write")
            self.assertNotEqual(0, malformed.returncode)
            self.assertFalse((root / ".claude").exists())

        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            (root / ".agents/skills/design-intake/templates/design-brief.md").unlink()
            missing = run_renderer(root, "--write")
            self.assertNotEqual(0, missing.returncode)
            self.assertFalse((root / ".claude").exists())

    def test_non_directory_output_ancestor_rejects_before_any_write(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            skills = root / ".claude/skills"
            skills.parent.mkdir(parents=True)
            skills.write_text("local file\n")
            result = run_renderer(root, "--write")
            self.assertNotEqual(0, result.returncode)
            self.assertIn("non-directory", result.stderr)
            self.assertEqual("local file\n", skills.read_text())
            self.assertFalse((root / ".claude/agents").exists())
            self.assertFalse((root / "agents/generated-host-files.json").exists())

    def test_directory_at_generated_file_path_is_preserved(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            collision = root / ".claude/agents/explorer.md"
            collision.mkdir(parents=True)
            result = run_renderer(root, "--write")
            self.assertNotEqual(0, result.returncode)
            self.assertIn("directory at generated file path", result.stderr)
            self.assertTrue(collision.is_dir())
            self.assertFalse((root / "agents/generated-host-files.json").exists())

    def test_manifest_path_escape_is_rejected_without_writes(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            (root / "agents/generated-host-files.json").write_text(
                json.dumps({"files": {"../outside": "0" * 64}})
            )
            result = run_renderer(root, "--write")
            self.assertNotEqual(0, result.returncode)
            self.assertIn("unsafe managed path", result.stderr)
            self.assertFalse((root / ".claude").exists())

    def test_manifest_path_outside_generated_host_namespace_is_rejected(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            (root / "agents/generated-host-files.json").write_text(
                json.dumps({"files": {"unmanaged.md": "0" * 64}})
            )
            result = run_renderer(root, "--write")
            self.assertNotEqual(0, result.returncode)
            self.assertIn("outside generated host namespace", result.stderr)
            self.assertFalse((root / ".claude").exists())

    def test_apply_failure_keeps_old_manifest(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            self.write_fixture(root)
            module = load_renderer(root)
            previous_manifest = (root / "agents/generated-host-files.json").read_bytes()
            outputs = module.render(root)
            outputs[".claude/agents/explorer.md"] += b"changed\n"
            outputs[".claude/agents/reviewer.md"] += b"changed\n"
            calls = 0

            def fail_after_one(path: Path, data: bytes) -> None:
                nonlocal calls
                calls += 1
                if calls == 2:
                    raise OSError("injected replacement failure")
                module.atomic_replace(path, data)

            with self.assertRaises(OSError):
                module.apply_changes(root, outputs, module.load_manifest(root), fail_after_one)
            self.assertEqual(previous_manifest, (root / "agents/generated-host-files.json").read_bytes())
            self.assertNotEqual(0, run_renderer(root, "--check").returncode)


if __name__ == "__main__":
    unittest.main()
