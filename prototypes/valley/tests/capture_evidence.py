from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "tests" / "evidence"
OUTPUT.mkdir(exist_ok=True)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    for name, viewport in (("desktop", {"width": 1280, "height": 900}), ("mobile", {"width": 390, "height": 844})):
        page = browser.new_page(viewport=viewport, device_scale_factor=1)
        page.goto((ROOT / "index.html").as_uri())
        page.wait_for_function("window.__valleyDebug !== undefined")
        page.wait_for_timeout(500)
        page.screenshot(path=str(OUTPUT / f"{name}.png"))
        page.close()
    browser.close()
