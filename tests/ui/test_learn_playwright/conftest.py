import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope="session")
def get_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="module")
def new_browser_context(get_browser):
    context = get_browser.new_context()
    yield context
    context.close()

@pytest.fixture
def new_page(new_browser_context):
    page = new_browser_context.new_page()
    yield page
    page.close()

