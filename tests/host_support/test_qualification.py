from __future__ import annotations

import re
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
ROUTES = (
    "design-intake",
    "gameplay-design",
    "system-design",
    "design-prototype",
    "design-review",
    "design-change",
)
ROLES = ("explorer", "worker", "tester", "reviewer", "researcher")
HOSTS = ("Codex", "Claude Code CLI", "agy CLI", "Antigravity app")
LIVE_CASES = (
    "all six routes",
    "all five roles",
    "direct skill invocation",
    "checkpoint 1",
    "checkpoint 2",
    "checkpoint 3",
    "each role invocation",
    "effective permissions",
    "native nested delegation excluded",
    "read-only write rejection",
    "worker/tester inherit roundtrip",
    "independent reviewer",
)


class QualificationTests(unittest.TestCase):
    def test_every_host_has_all_routes_and_roles(self) -> None:
        readme = (REPOSITORY_ROOT / "README.md").read_text()
        evidence = (REPOSITORY_ROOT / "tests/behavior/multi-host-support.md").read_text()

        for route in ROUTES:
            self.assertTrue((REPOSITORY_ROOT / ".agents/skills" / route).is_dir())
            self.assertIn(route, readme)
            self.assertIn(route, evidence)
        for role in ROLES:
            self.assertTrue((REPOSITORY_ROOT / ".codex/agents" / f"{role}.toml").is_file())
            self.assertTrue((REPOSITORY_ROOT / ".claude/agents" / f"{role}.md").is_file())
            self.assertTrue((REPOSITORY_ROOT / ".agents/agents" / f"{role}.md").is_file())
            self.assertIn(role, readme)
            self.assertIn(role, evidence)
        for host in HOSTS:
            self.assertIn(f"| {host} |", evidence)

    def test_no_unscoped_or_foreign_host_configuration(self) -> None:
        readme = (REPOSITORY_ROOT / "README.md").read_text().lower()
        policy = (REPOSITORY_ROOT / "agents/orchestration.md").read_text().lower()

        self.assertIn("global configuration", readme)
        self.assertIn("active cli/session identity", policy)
        self.assertIn("directory presence", policy)
        self.assertIn("does not install anything globally", readme)

        for role in ROLES:
            claude = (REPOSITORY_ROOT / ".claude/agents" / f"{role}.md").read_text()
            antigravity = (REPOSITORY_ROOT / ".agents/agents" / f"{role}.md").read_text()
            codex = (REPOSITORY_ROOT / ".codex/agents" / f"{role}.toml").read_text()
            self.assertNotIn("model_reasoning_effort", claude)
            self.assertNotIn("sandbox_mode", claude)
            self.assertNotIn("permissionMode", antigravity)
            self.assertNotIn("model_reasoning_effort", antigravity)
            self.assertNotIn("sandbox_mode", antigravity)
            self.assertNotIn("permissionMode", codex)

    def test_no_runtime_verification_claim_without_evidence(self) -> None:
        evidence = (REPOSITORY_ROOT / "tests/behavior/multi-host-support.md").read_text()
        statuses = re.findall(
            r"^\| (Codex|Claude Code CLI|agy CLI|Antigravity app) \| "
            r"(configured|runtime-verified|blocked) \|",
            evidence,
            re.MULTILINE,
        )
        self.assertEqual(set(HOSTS), {host for host, _ in statuses})
        self.assertTrue(statuses)
        matrix_header = next(
            line for line in evidence.splitlines() if line.startswith("| Host | all six routes |")
        )
        self.assertEqual(matrix_header.count("|") - 1, len(LIVE_CASES) + 1)
        for host in HOSTS:
            section = re.search(
                rf"^### {re.escape(host)} case records$.*?(?=^### |\Z)",
                evidence,
                re.MULTILINE | re.DOTALL,
            )
            self.assertIsNotNone(section)
            host_evidence = section.group(0)
            self.assertRegex(
                evidence,
                re.compile(
                    rf"^\| {re.escape(host)} \|(?: [^|]+ \|){{{len(LIVE_CASES)}}}$",
                    re.MULTILINE,
                ),
            )
            self.assertRegex(
                evidence,
                re.compile(
                    rf"^### {re.escape(host)} case records$.*?^\| Case \| Result \| Command or input \| Observed output \| Artifact path \|$",
                    re.MULTILINE | re.DOTALL,
                ),
            )
            for case in LIVE_CASES:
                self.assertRegex(
                    host_evidence,
                    re.compile(
                        rf"^\| {re.escape(case)} \| (?:NOT RUN|PASS|FAIL) \|",
                        re.MULTILINE,
                    ),
                )
        for host, status in statuses:
            if status == "runtime-verified":
                section = re.search(
                    rf"^### {re.escape(host)} case records$.*?(?=^### |\Z)",
                    evidence,
                    re.MULTILINE | re.DOTALL,
                )
                self.assertIsNotNone(section)
                self.assertNotIn("NOT RUN", section.group(0))
        self.assertIn("not run", evidence.lower())
        self.assertIn("configured", evidence.lower())

    def test_antigravity_tool_qualification_is_documented(self) -> None:
        evidence = (REPOSITORY_ROOT / "tests/behavior/multi-host-support.md").read_text()
        metadata = (REPOSITORY_ROOT / "agents/host-adapters.json").read_text()

        self.assertIn("https://antigravity.google/docs/subagents/", evidence)
        self.assertIn("https://antigravity.google/docs/hooks", evidence)
        self.assertIn("docs/research/2026-10-12-multi-host-orchestration.md", evidence)
        self.assertIn("docs/research/2026-10-12-multi-host-instruction-discovery.md", evidence)
        self.assertIn("no live schema or session test ran", evidence.lower())
        self.assertIn("configured, not runtime-verified", evidence.lower())
        for tool in (
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
        ):
            self.assertIn(f"`{tool}`", evidence)
            self.assertIn(f'"{tool}"', metadata)


if __name__ == "__main__":
    unittest.main()
