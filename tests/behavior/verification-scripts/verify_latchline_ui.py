from __future__ import annotations

import os
from itertools import product
from pathlib import Path

os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/tmp/game-designer-browsers")

from playwright.sync_api import sync_playwright


ROOT = Path("/data/lea/Workspace/game_designer")
GAME = (ROOT / "prototypes/salvage/index.html").as_uri()
SCREENSHOTS = ROOT / ".superpowers/sdd/2026-09-30-game-designer/final-browser"

EXPECTED = {
    ("Retrieve", "Stabilize", "Retrieve"): (1, 5, "extracted", "extracted"),
    ("Retrieve", "Stabilize", "Mark"): (4, 2, "lost", "cargo-target-missed"),
    ("Retrieve", "Strip", "Retrieve"): (0, 6, "lost", "hull-breach"),
    ("Retrieve", "Strip", "Mark"): (3, 3, "lost", "cargo-target-missed"),
    ("Mark", "Stabilize", "Retrieve"): (1, 3, "lost", "cargo-target-missed"),
    ("Mark", "Stabilize", "Mark"): (4, 0, "lost", "cargo-target-missed"),
    ("Mark", "Strip", "Retrieve"): (1, 4, "lost", "cargo-target-missed"),
    ("Mark", "Strip", "Mark"): (4, 1, "lost", "cargo-target-missed"),
}


def signed(value: int) -> str:
    return f"+{value}" if value >= 0 else str(value)


def verify_sequence(page, sequence):
    errors = []
    page.on("console", lambda message: errors.append(message.text) if message.type == "error" else None)
    page.goto(GAME, wait_until="load")
    for action in sequence:
        page.get_by_role("button", name=action, exact=True).click()
    state = page.evaluate("window.LatchlineSalvage.getState()")
    expected = EXPECTED[sequence]
    assert (state["hull"], state["cargo"], state["status"], state["events"][-1]["outcome"]) == expected, state
    assert [event["order"] for event in state["events"]] == [1, 2, 3], state
    assert page.locator("#event-log li").count() == 3
    previous = {"hull": 4, "cargo": 0}
    for index, event in enumerate(state["events"]):
        expected_delta = f"Cargo {signed(event['cargo'] - previous['cargo'])} / Hull {signed(event['hull'] - previous['hull'])}"
        assert expected_delta in page.locator("#event-log li").nth(index).inner_text(), (sequence, index, expected_delta)
        previous = event
    if expected[2] == "extracted":
        assert "Extraction successful" in page.locator("#terminal").inner_text()
    elif expected[3] == "hull-breach":
        assert "Hull breach: run lost" in page.locator("#terminal").inner_text()
    else:
        assert "Cargo target missed: run lost" in page.locator("#terminal").inner_text()
    page.get_by_role("button", name="Restart run", exact=True).click()
    reset = page.evaluate("window.LatchlineSalvage.getState()")
    assert reset == {"section": 1, "hull": 4, "cargo": 0, "status": "active", "events": []}, reset
    assert page.locator("#event-log li").count() == 0
    assert "No actions resolved" in page.locator("#latest-result").inner_text()
    assert not errors, errors
    return state


def main():
    SCREENSHOTS.mkdir(parents=True, exist_ok=True)
    results = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        for sequence in product(("Retrieve", "Mark"), ("Stabilize", "Strip"), ("Retrieve", "Mark")):
            page = browser.new_page(viewport={"width": 1280, "height": 900})
            state = verify_sequence(page, sequence)
            results.append(("-".join(sequence), state["hull"], state["cargo"], state["status"], state["events"][-1]["outcome"]))
            page.close()

        for name, viewport, sequence in (
            ("desktop-1280x900", {"width": 1280, "height": 900}, ("Retrieve", "Stabilize", "Retrieve")),
            ("mobile-390x844", {"width": 390, "height": 844}, ("Retrieve", "Strip", "Retrieve")),
            ("narrow-320x568", {"width": 320, "height": 568}, ("Mark", "Strip", "Mark")),
        ):
            page = browser.new_page(viewport=viewport)
            errors = []
            page.on("console", lambda message: errors.append(message.text) if message.type == "error" else None)
            page.goto(GAME, wait_until="load")
            svg = page.locator(".wreck svg")
            box = svg.bounding_box()
            assert box and box["width"] > 0 and box["height"] > 0, (name, box)
            assert page.locator(".wreck svg path").count() >= 3
            assert page.evaluate("getComputedStyle(document.querySelector('.wreck svg')).visibility") == "visible"
            for action in sequence:
                page.get_by_role("button", name=action, exact=True).click()
            dimensions = page.evaluate("({scrollWidth: document.documentElement.scrollWidth, clientWidth: document.documentElement.clientWidth, bodyScrollWidth: document.body.scrollWidth})")
            assert dimensions["scrollWidth"] <= dimensions["clientWidth"], (name, dimensions)
            assert dimensions["bodyScrollWidth"] <= dimensions["clientWidth"], (name, dimensions)
            assert not errors, (name, errors)
            page.screenshot(path=str(SCREENSHOTS / f"{name}.png"), full_page=True)
            print(f"VIEWPORT {name} svg={box['width']:.0f}x{box['height']:.0f} overflow={dimensions} console_errors=0")
            page.close()
        browser.close()
    for result in results:
        print("SEQUENCE", *result)
    print(f"PASS sequences={len(results)} viewports=3 screenshots=3")


if __name__ == "__main__":
    main()
