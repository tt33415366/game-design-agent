from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
BASELINE_PATH = REPOSITORY_ROOT / "tests/host_support/preservation-baseline.json"
CANONICAL_FILES = (
    ".codex/config.toml",
    "agents/game-designer.md",
)
CANONICAL_TREES = (
    ".codex/agents",
    ".agents/skills/design-intake",
    ".agents/skills/gameplay-design",
    ".agents/skills/system-design",
    ".agents/skills/design-prototype",
    ".agents/skills/design-review",
    ".agents/skills/design-change",
)


def canonical_source_paths(root: Path) -> set[str]:
    paths = {path for path in CANONICAL_FILES if (root / path).is_file()}
    for tree in CANONICAL_TREES:
        tree_path = root / tree
        if tree_path.exists():
            paths.update(
                path.relative_to(root).as_posix()
                for path in tree_path.rglob("*")
                if path.is_file()
            )
    return paths


def canonical_source_differences(root: Path, baseline: dict[str, str]) -> list[str]:
    expected_paths = set(baseline)
    actual_paths = canonical_source_paths(root)
    differences = [f"missing {path}" for path in sorted(expected_paths - actual_paths)]
    differences.extend(f"added {path}" for path in sorted(actual_paths - expected_paths))
    for path in sorted(expected_paths & actual_paths):
        digest = hashlib.sha256((root / path).read_bytes()).hexdigest()
        if digest != baseline[path]:
            differences.append(f"modified {path}")
    return differences


class SharedContractTests(unittest.TestCase):
    def load_baseline(self) -> dict[str, str]:
        return json.loads(BASELINE_PATH.read_text())["files"]

    def test_shared_routing(self) -> None:
        root_instructions = (REPOSITORY_ROOT / "AGENTS.md").read_text()
        policy = (REPOSITORY_ROOT / "agents/orchestration.md").read_text()

        self.assertIn("agents/orchestration.md", root_instructions)
        self.assertIn("complex", root_instructions.lower())
        self.assertIn("agents/game-designer.md", root_instructions)
        self.assertIn("bounded context", policy)
        self.assertIn("single writer", policy)
        self.assertIn("publication", policy.lower())

    def test_codex_profile_unchanged(self) -> None:
        baseline = self.load_baseline()
        codex_paths = {path: digest for path, digest in baseline.items() if path.startswith(".codex/")}
        changed = [
            path
            for path, digest in codex_paths.items()
            if hashlib.sha256((REPOSITORY_ROOT / path).read_bytes()).hexdigest() != digest
        ]
        self.assertEqual([], changed)

    def test_missing_delegation_is_not_independent_review(self) -> None:
        policy = (REPOSITORY_ROOT / "agents/orchestration.md").read_text().lower()
        normalized_policy = " ".join(policy.split())

        self.assertIn("unavailable", policy)
        self.assertIn("cannot satisfy independent review", normalized_policy)
        self.assertIn("self-check", policy)

    def test_host_selection_uses_session_identity(self) -> None:
        policy = (REPOSITORY_ROOT / "agents/orchestration.md").read_text().lower()

        self.assertIn("active cli/session identity", policy)
        self.assertIn("do not infer", policy)
        self.assertIn("directory presence", policy)

    def test_link_audit_uses_its_checkout(self) -> None:
        source = REPOSITORY_ROOT / "tests/behavior/verification-scripts/check_game_designer_links.py"
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary = Path(temporary_directory)
            checkout = temporary / "checkout copy"
            checker = checkout / "tests/behavior/verification-scripts/check_game_designer_links.py"
            checker.parent.mkdir(parents=True)
            shutil.copy2(source, checker)
            (checkout / "guide.md").write_text("[target](target.md)\n")
            (checkout / "target.md").write_text("target\n")

            result = subprocess.run(
                [sys.executable, str(checker)],
                cwd=temporary,
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("LINK_AUDIT files=2 local_targets=1 broken=0", result.stdout)

    def test_canonical_sources_match_baseline(self) -> None:
        self.assertEqual([], canonical_source_differences(REPOSITORY_ROOT, self.load_baseline()))

    def test_canonical_source_changes_fail_against_baseline(self) -> None:
        baseline = self.load_baseline()
        with tempfile.TemporaryDirectory() as temporary_directory:
            fixture_root = Path(temporary_directory)
            for path in baseline:
                destination = fixture_root / path
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(REPOSITORY_ROOT / path, destination)

            changed_path = next(iter(sorted(baseline)))
            (fixture_root / changed_path).write_text("changed\n")
            self.assertIn(
                f"modified {changed_path}",
                canonical_source_differences(fixture_root, baseline),
            )

            (fixture_root / changed_path).unlink()
            self.assertIn(
                f"missing {changed_path}",
                canonical_source_differences(fixture_root, baseline),
            )

            added_path = ".agents/skills/design-intake/unexpected.md"
            added = fixture_root / added_path
            added.parent.mkdir(parents=True, exist_ok=True)
            added.write_text("unexpected\n")
            self.assertIn(
                f"added {added_path}",
                canonical_source_differences(fixture_root, baseline),
            )


if __name__ == "__main__":
    unittest.main()
