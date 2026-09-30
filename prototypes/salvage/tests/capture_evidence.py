"""Capture repeatable Latchline Salvage browser evidence without a web server."""

from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/tmp/game-designer-browsers")

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
GAME = (ROOT / "index.html").as_uri()
EVIDENCE = ROOT / "evidence"


def assert_visible_run(page, actions, terminal_text):
    for action in actions:
        page.get_by_role("button", name=action, exact=True).click()
    assert terminal_text in page.locator("#terminal").inner_text()


def check_page(page, size, name):
    errors = []
    page.on("console", lambda message: errors.append(message.text) if message.type == "error" else None)
    page.goto(GAME)
    assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth")
    before = page.evaluate("window.LatchlineSalvage.getState()")
    page.evaluate("window.LatchlineSalvage.render()")
    assert page.evaluate("window.LatchlineSalvage.getState()") == before
    page.screenshot(path=str(EVIDENCE / name), full_page=True)
    assert errors == []


def main():
    EVIDENCE.mkdir(exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        desktop = browser.new_page(viewport={"width": 1280, "height": 800})
        check_page(desktop, (1280, 800), "desktop-initial.png")
        assert_visible_run(desktop, ["Retrieve", "Stabilize", "Retrieve"], "Extraction successful")
        desktop.screenshot(path=str(EVIDENCE / "desktop-extracted.png"), full_page=True)

        hull_loss = browser.new_page(viewport={"width": 1280, "height": 800})
        hull_loss.goto(GAME)
        assert_visible_run(hull_loss, ["Retrieve", "Strip", "Retrieve"], "Hull breach: run lost")

        cargo_loss = browser.new_page(viewport={"width": 1280, "height": 800})
        cargo_loss.goto(GAME)
        assert_visible_run(cargo_loss, ["Mark", "Stabilize", "Mark"], "Cargo target missed: run lost")

        mobile = browser.new_page(viewport={"width": 390, "height": 844})
        check_page(mobile, (390, 844), "mobile-initial.png")
        browser.close()
    print("Evidence checks passed: desktop/mobile no overflow, no console errors, render no state change, and three terminal paths.")


if __name__ == "__main__":
    main()
