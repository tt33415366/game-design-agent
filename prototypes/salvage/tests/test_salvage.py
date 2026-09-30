"""Browser-executed verification for the authoritative Latchline Salvage rules."""

from __future__ import annotations

import os
import unittest
from pathlib import Path

os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/tmp/game-designer-browsers")

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
HARNESS = (ROOT / "tests" / "rules-harness.html").as_uri()
GAME = (ROOT / "index.html").as_uri()
RULES = ROOT / "salvage-rules.js"
APP = ROOT / "index.html"


class SalvageAvailabilityTest(unittest.TestCase):
    def test_rules_module_is_available_to_the_browser(self):
        self.assertTrue(RULES.exists(), "Latchline Salvage needs its reusable browser rules module")


@unittest.skipUnless(RULES.exists(), "rules module is not implemented yet")
class SalvageRuleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=True)
        cls.page = cls.browser.new_page()
        cls.page.goto(HARNESS)
        cls.page.wait_for_function("typeof window.LatchlineRules !== 'undefined'")

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def resolve(self, actions):
        return self.page.evaluate(
            """actions => actions.reduce(
                (state, action) => window.LatchlineRules.applyAction(state, action),
                window.LatchlineRules.startRun()
            )""",
            actions,
        )

    def test_v01_safe_sequence_extracts_with_three_ordered_events(self):
        state = self.resolve(["Retrieve", "Stabilize", "Retrieve"])
        self.assertEqual((state["section"], state["hull"], state["cargo"], state["status"]), (3, 1, 5, "extracted"))
        self.assertEqual([event["order"] for event in state["events"]], [1, 2, 3])
        self.assertEqual(state["events"][-1]["outcome"], "extracted")

    def test_v02_hull_breach_overrides_cargo_extraction(self):
        state = self.resolve(["Retrieve", "Strip", "Retrieve"])
        self.assertEqual((state["hull"], state["cargo"], state["status"]), (0, 6, "lost"))
        self.assertEqual(state["events"][-1], {
            "order": 3, "section": 3, "action": "Retrieve", "hull": 0,
            "cargo": 6, "status": "lost", "outcome": "hull-breach",
        })

    def test_v03_cargo_target_miss_loses_after_surviving_reactor(self):
        state = self.resolve(["Mark", "Stabilize", "Mark"])
        self.assertEqual((state["hull"], state["cargo"], state["status"]), (4, 0, "lost"))
        self.assertEqual(state["events"][-1]["outcome"], "cargo-target-missed")

    def test_v04_invalid_input_preserves_state_and_latest_event(self):
        state = self.resolve(["Retrieve"])
        invalid = self.page.evaluate(
            "state => window.LatchlineRules.applyAction(state, 'Retrieve')", state
        )
        self.assertEqual(invalid, state)
        self.assertEqual((invalid["section"], invalid["hull"], invalid["cargo"], invalid["status"]), (2, 3, 2, "active"))
        self.assertEqual(len(invalid["events"]), 1)

    def test_v05_restart_replaces_prior_state_and_events(self):
        prior = self.resolve(["Retrieve"])
        reset = self.page.evaluate("state => window.LatchlineRules.startRun(state)", prior)
        self.assertEqual(reset, {"section": 1, "hull": 4, "cargo": 0, "status": "active", "events": []})

    def test_hull_recovery_is_capped_and_terminal_input_is_a_no_op(self):
        state = self.resolve(["Mark", "Stabilize"])
        self.assertEqual(state["hull"], 4)
        terminal = self.resolve(["Retrieve", "Strip", "Retrieve"])
        ignored = self.page.evaluate(
            "state => window.LatchlineRules.applyAction(state, 'Mark')", terminal
        )
        self.assertEqual(ignored, terminal)


@unittest.skipUnless(APP.exists(), "browser interface is not implemented yet")
class SalvageInterfaceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=True)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def test_schematic_legend_is_visible_and_fits_desktop_and_mobile(self):
        for width, height in ((1280, 900), (390, 844), (320, 568)):
            with self.subTest(width=width):
                page = self.browser.new_page(viewport={"width": width, "height": height})
                try:
                    page.goto(GAME)
                    legend = page.get_by_role("figure", name="Wreck schematic")
                    self.assertEqual(legend.count(), 1)
                    self.assertTrue(legend.is_visible())
                    for label in ("Hull outline", "Internal structure", "Reactor", "Damage markers", "Scan line"):
                        self.assertTrue(legend.get_by_text(label, exact=True).is_visible())
                    self.assertIn("Not a live status display", legend.inner_text())
                    self.assertTrue(page.evaluate("document.documentElement.scrollWidth <= innerWidth"))
                    drawing = legend.locator(".viewport").bounding_box()
                    caption = legend.locator("figcaption").bounding_box()
                    self.assertGreaterEqual(caption["y"], drawing["y"] + drawing["height"])
                finally:
                    page.close()

    def test_ui_plays_to_extraction_then_restart_clears_visible_log(self):
        page = self.browser.new_page(viewport={"width": 1280, "height": 800})
        errors = []
        page.on("console", lambda message: errors.append(message.text) if message.type == "error" else None)
        page.goto(GAME)
        page.get_by_role("button", name="Retrieve").click()
        before_refresh = page.evaluate("window.LatchlineSalvage.getState()")
        page.evaluate("window.LatchlineSalvage.render()")
        self.assertEqual(page.evaluate("window.LatchlineSalvage.getState()"), before_refresh)
        page.get_by_role("button", name="Stabilize").click()
        page.get_by_role("button", name="Retrieve").click()
        self.assertIn("Extraction successful", page.locator("#terminal").inner_text())
        self.assertIn("Final cargo 5/5 target, hull 1/4", page.locator("#terminal").inner_text())
        self.assertIn("Hull: 1/4", page.locator("#hull").inner_text())
        self.assertIn("Cargo: 5", page.locator("#cargo").inner_text())
        self.assertEqual(page.locator("#event-log li").count(), 3)
        page.get_by_role("button", name="Restart run").click()
        self.assertIn("No actions resolved", page.locator("#latest-result").inner_text())
        self.assertEqual(page.locator("#event-log li").count(), 0)
        self.assertEqual(errors, [])

    def test_ui_shows_route_and_non_mutating_action_previews(self):
        page = self.browser.new_page(viewport={"width": 320, "height": 568})
        page.goto(GAME)
        self.assertIn("CURRENT\nCargo Hold", page.locator("#route").inner_text())
        self.assertIn("UPCOMING\nRelay", page.locator("#route").inner_text())
        self.assertIn("UPCOMING\nReactor", page.locator("#route").inner_text())
        before_preview = page.evaluate("window.LatchlineSalvage.getState()")
        retrieve = page.get_by_role("button", name="Retrieve")
        self.assertEqual(retrieve.get_attribute("aria-describedby"), "preview-retrieve")
        self.assertIn("Cargo +2 / Hull -1", page.locator("#preview-retrieve").inner_text())
        self.assertIn("Cargo +0 / Hull +0", page.locator("#preview-mark").inner_text())
        self.assertEqual(page.evaluate("window.LatchlineSalvage.getState()"), before_preview)
        retrieve.click()
        self.assertIn("COMPLETED\nCargo Hold", page.locator("#route").inner_text())
        self.assertIn("CURRENT\nRelay", page.locator("#route").inner_text())
        self.assertIn("UPCOMING\nReactor", page.locator("#route").inner_text())
        self.assertTrue(page.evaluate("document.documentElement.scrollWidth <= innerWidth"))

    def test_terminal_explanations_show_final_resources_and_priority(self):
        page = self.browser.new_page(viewport={"width": 320, "height": 568})
        page.goto(GAME)
        page.get_by_role("button", name="Retrieve").click()
        page.get_by_role("button", name="Strip").click()
        page.get_by_role("button", name="Retrieve").click()
        terminal = page.locator("#terminal").inner_text()
        self.assertIn("Final cargo 6/5 target, hull 0/4", terminal)
        self.assertIn("Hull breach takes priority", terminal)
        self.assertTrue(page.evaluate("document.documentElement.scrollWidth <= innerWidth"))
        self.assertIn("Run complete", page.locator("#preview-retrieve").inner_text())
        page.get_by_role("button", name="Restart run").click()
        page.get_by_role("button", name="Mark").click()
        page.get_by_role("button", name="Stabilize").click()
        page.get_by_role("button", name="Mark").click()
        terminal = page.locator("#terminal").inner_text()
        self.assertIn("Final cargo 0/5 target, hull 4/4", terminal)
        self.assertIn("Hull survived, but cargo did not reach 5", terminal)
        self.assertTrue(page.evaluate("document.documentElement.scrollWidth <= innerWidth"))

    def test_ui_log_shows_action_deltas_including_capped_recovery(self):
        page = self.browser.new_page(viewport={"width": 1280, "height": 800})
        page.goto(GAME)
        page.get_by_role("button", name="Retrieve").click()
        self.assertIn("Cargo +2 / Hull -1", page.locator("#event-log li").nth(0).inner_text())
        page.get_by_role("button", name="Stabilize").click()
        self.assertIn("Cargo +0 / Hull +1", page.locator("#event-log li").nth(1).inner_text())
        page.get_by_role("button", name="Restart run").click()
        page.get_by_role("button", name="Mark").click()
        page.get_by_role("button", name="Stabilize").click()
        self.assertIn("Cargo +0 / Hull +0", page.locator("#event-log li").nth(1).inner_text())


if __name__ == "__main__":
    unittest.main(verbosity=2)
