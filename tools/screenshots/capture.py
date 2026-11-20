"""@file
@brief Starts the app and takes one screenshot per build step with a headless browser.

Runs inside the container built from tools/screenshots/Dockerfile.
"""

import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

from playwright.sync_api import Page, sync_playwright

URL = "http://127.0.0.1:5000/"
OUT_DIR = Path(os.environ.get("OUT_DIR", "/out"))
SAMPLE_TEXT = "It was a quiet morning, and the words finally started to come"


def wait_for_server() -> None:
    """@brief Wait until the app answers, or stop after 20 seconds."""
    for _ in range(100):
        try:
            urllib.request.urlopen(URL, timeout=1).close()
            return
        except OSError:
            time.sleep(0.2)
    raise RuntimeError("the app did not start")


def wait_for_state(page: Page, state: str) -> None:
    """@brief Wait until the page shows the given state class.

    @param page The browser page.
    @param state The state class name, for example state-warning.
    """
    page.wait_for_function(
        "state => document.body.dataset.state === state", arg=state, timeout=15000
    )


def capture(page: Page, name: str) -> None:
    """@brief Save a screenshot.

    @param page The browser page.
    @param name The file name without folder.
    """
    page.screenshot(path=str(OUT_DIR / name))
    sys.stdout.write(f"saved {name}\n")


def main() -> None:
    """@brief Take the four step screenshots."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    server = subprocess.Popen([sys.executable, "-m", "disappearing_text"])
    try:
        wait_for_server()
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page(viewport={"width": 900, "height": 600})
            page.goto(URL)
            capture(page, "step-1-empty-editor.png")
            page.locator("#editor").press_sequentially(SAMPLE_TEXT, delay=20)
            wait_for_state(page, "state-typing")
            capture(page, "step-2-typing-with-countdown.png")
            wait_for_state(page, "state-warning")
            capture(page, "step-3-warning-last-seconds.png")
            wait_for_state(page, "state-gone")
            capture(page, "step-4-text-gone.png")
            browser.close()
    finally:
        server.terminate()
        server.wait(timeout=10)


if __name__ == "__main__":
    main()
