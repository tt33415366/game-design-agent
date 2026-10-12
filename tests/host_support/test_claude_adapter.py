from __future__ import annotations

import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


class ClaudeAdapterTests(unittest.TestCase):
    def test_hand_maintained_entry_point_imports_root_instructions(self) -> None:
        self.assertEqual("@AGENTS.md\n", (REPOSITORY_ROOT / "CLAUDE.md").read_text())


if __name__ == "__main__":
    unittest.main()
