import pytest
import random, os, sys
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption(
        "--test-browser",
        action="store",
        default="random",
        help="Choose browser: chrome, edge, firefox, or random"
    )

@pytest.fixture(scope="session")
def browser_context_args(pytestconfig):
    width, height = 1920, 1080
    return {"width": width, "height": height}

@pytest.fixture(scope="session")
def browser(pytestconfig, browser_context_args):
    browser_choice = pytestconfig.getoption("--test-browser")

    if browser_choice == "random":
        browser_choice = random.choice(["chrome", "edge", "firefox"])

    width, height = browser_context_args["width"], browser_context_args["height"]

    playwright = sync_playwright().start()

    if browser_choice == "chrome":
        browser = playwright.chromium.launch(headless=False, channel="chrome", args=[
            f"--window-size={width},{height}"
        ])
    elif browser_choice == "edge":
        browser = playwright.chromium.launch(headless=False, channel="msedge", args=[
            f"--window-size={width},{height}"
        ])
    elif browser_choice == "firefox":
        browser = playwright.firefox.launch(headless=False)
    else:
        raise ValueError(f"❌ Unsupported browser: {browser_choice}")

    print(f"\n✅ Launched browser: {browser_choice.upper()} with resolution {width}x{height}")
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture(scope="function")
def page(browser, browser_context_args):
    width, height = browser_context_args["width"], browser_context_args["height"]

    context = browser.new_context(
        viewport={"width": width, "height": height},
        screen={"width": width, "height": height}
    )
    page = context.new_page()
    yield page
    page.close()
    context.close()