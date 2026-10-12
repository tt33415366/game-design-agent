from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = REPOSITORY_ROOT / "scripts/sync_host_adapters.py"
ROLES = ("explorer", "researcher", "reviewer", "tester", "worker")
READ_ONLY_TOOLS = '["view_file", "list_dir", "find_by_name", "grep_search"]'
RESEARCH_TOOLS = (
    '["view_file", "list_dir", "find_by_name", "grep_search", '
    '"search_web", "read_url_content"]'
)


def fixture_repository() -> tempfile.TemporaryDirectory[str]:
    temporary = tempfile.TemporaryDirectory(prefix="antigravity adapter ")
    root = Path(temporary.name) / "repository with spaces"
    (root / "scripts").mkdir(parents=True)
    shutil.copy2(SCRIPT, root / "scripts/sync_host_adapters.py")
    shutil.copytree(REPOSITORY_ROOT / "agents", root / "agents")
    shutil.copytree(REPOSITORY_ROOT / ".codex/agents", root / ".codex/agents")
    shutil.copytree(REPOSITORY_ROOT / ".agents/skills", root / ".agents/skills")
    shutil.copytree(REPOSITORY_ROOT / ".claude", root / ".claude")
    return temporary


def run_renderer(root: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(root / "scripts/sync_host_adapters.py"), *arguments],
        cwd=Path.cwd(),
        capture_output=True,
        text=True,
        check=False,
    )


class AntigravityAdapterTests(unittest.TestCase):
    def write_fixture(self, root: Path) -> None:
        result = run_renderer(root, "--write")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_all_five_roles(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            claude_before = {
                path.relative_to(root): path.read_bytes()
                for path in (root / ".claude").rglob("*")
                if path.is_file()
            }

            self.write_fixture(root)

            self.assertEqual(
                {f".agents/agents/{role}.md" for role in ROLES},
                {
                    path.relative_to(root).as_posix()
                    for path in (root / ".agents/agents").glob("*.md")
                },
            )
            self.assertEqual(
                claude_before,
                {
                    path.relative_to(root): path.read_bytes()
                    for path in (root / ".claude").rglob("*")
                    if path.is_file()
                },
            )
            manifest = json.loads((root / "agents/generated-host-files.json").read_text())
            self.assertTrue({f".agents/agents/{role}.md" for role in ROLES} <= set(manifest["files"]))

    def test_native_subagent_fields(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            self.write_fixture(root)

            for role in ROLES:
                frontmatter = (root / f".agents/agents/{role}.md").read_text().split("---", 2)[1]
                self.assertIn(f'name: "{role}"', frontmatter)
                self.assertIn("model: inherit", frontmatter)
                self.assertIn("subagent: true", frontmatter)
                self.assertIn("mainAgent: false", frontmatter)
                self.assertIn("commandExecutionPolicy: sandbox", frontmatter)

    def test_read_only_roles_have_no_command_or_write_tools(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            self.write_fixture(root)

            forbidden = {
                "write_to_file",
                "replace_file_content",
                "multi_replace_file_content",
                "run_command",
                "manage_task",
            }
            for role in ("explorer", "reviewer"):
                content = (root / f".agents/agents/{role}.md").read_text()
                self.assertIn(f"tools: {READ_ONLY_TOOLS}", content)
                self.assertFalse(any(tool in content for tool in forbidden))

    def test_all_roles_exclude_native_delegation(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            self.write_fixture(root)

            forbidden = {"invoke_subagent", "define_subagent", "send_message", "manage_subagents"}
            for role in ROLES:
                content = (root / f".agents/agents/{role}.md").read_text()
                self.assertFalse(any(tool in content for tool in forbidden))

    def test_researcher_can_search_without_mutation(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            self.write_fixture(root)

            content = (root / ".agents/agents/researcher.md").read_text()
            self.assertIn(f"tools: {RESEARCH_TOOLS}", content)
            for tool in ("write_to_file", "replace_file_content", "multi_replace_file_content", "run_command"):
                self.assertNotIn(tool, content)

    def test_codex_model_fields_absent(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            self.write_fixture(root)

            for role in ROLES:
                frontmatter = (root / f".agents/agents/{role}.md").read_text().split("---", 2)[1]
                self.assertNotIn("model_reasoning_effort", frontmatter)
                self.assertNotIn("sandbox_mode", frontmatter)

    def test_shared_skill_tree_is_not_copied(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            skills_before = {
                path.relative_to(root): path.read_bytes()
                for path in (root / ".agents/skills").rglob("*")
                if path.is_file()
            }

            self.write_fixture(root)

            self.assertEqual(skills_before, {
                path.relative_to(root): path.read_bytes()
                for path in (root / ".agents/skills").rglob("*")
                if path.is_file()
            })
            manifest = json.loads((root / "agents/generated-host-files.json").read_text())
            self.assertFalse(any(path.startswith(".agents/skills/") for path in manifest["files"]))

    def test_unknown_native_tool_is_rejected_before_writes(self) -> None:
        with fixture_repository() as temporary:
            root = Path(temporary) / "repository with spaces"
            metadata_path = root / "agents/host-adapters.json"
            metadata = json.loads(metadata_path.read_text())
            metadata["antigravity"]["roles"]["explorer"]["tools"].append("unsupported_tool")
            metadata_path.write_text(json.dumps(metadata))

            result = run_renderer(root, "--write")

            self.assertNotEqual(0, result.returncode)
            self.assertIn("unsupported Antigravity tool for explorer", result.stderr)
            self.assertFalse((root / ".agents/agents").exists())
            self.assertEqual(
                (REPOSITORY_ROOT / "agents/generated-host-files.json").read_bytes(),
                (root / "agents/generated-host-files.json").read_bytes(),
            )


if __name__ == "__main__":
    unittest.main()
