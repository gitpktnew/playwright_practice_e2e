import re
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.fixture(scope="session")
def get_bowser():
    with sync_playwright() as playwright:
        # browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        browser = playwright.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def get_context(get_bowser):
    context = get_bowser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function", autouse=True)
def new_page(request, get_context):
    page = get_context.new_page()
    yield page
    page.close()

@pytest.mark.ui
def test_check_demo_mvc1(new_page):
    new_page.goto("https://demo.playwright.dev/todomvc/#/")
    new_page.get_by_role("textbox", name="What needs to be done?").click()
    new_page.get_by_role("textbox", name="What needs to be done?").fill("feed the dog")
    new_page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    new_page.get_by_role("textbox", name="What needs to be done?").fill("water the plants")
    new_page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    new_page.get_by_role("textbox", name="What needs to be done?").fill("buy chocolates")
    new_page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    new_page.get_by_role("listitem").filter(has_text="water the plants").get_by_label("Toggle Todo").check()
    expect(new_page.get_by_text("water the plants")).to_be_visible()
    new_page.get_by_role("link", name="Active").click()
    expect(new_page.get_by_text("feed the dog")).to_be_visible()
    expect(new_page.get_by_text("buy chocolates")).to_be_visible()
    new_page.get_by_role("button", name="Clear completed").click()
    expect(new_page.get_by_role("heading", name="todos")).to_be_visible()  

@pytest.mark.ui
def test_check_demo_mvc2(new_page):
    new_page.goto("https://demo.playwright.dev/todomvc/#/")
    new_page.get_by_role("textbox", name="What needs to be done?").click()
    new_page.get_by_role("textbox", name="What needs to be done?").fill("get up")
    new_page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    new_page.get_by_role("textbox", name="What needs to be done?").fill("get ready for school")
    new_page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    new_page.get_by_role("textbox", name="What needs to be done?").fill("go to school")
    new_page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    new_page.get_by_role("listitem").filter(has_text="get ready for school").get_by_label("Toggle Todo").check()
    expect(new_page.get_by_text("get ready for school")).to_be_visible()
    new_page.get_by_role("link", name="Active").click()
    expect(new_page.get_by_text("get up")).to_be_visible()
    expect(new_page.get_by_text("go to school")).to_be_visible()
    new_page.get_by_role("button", name="Clear completed").click()
    expect(new_page.get_by_role("heading", name="todos")).to_be_visible()


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://demo.playwright.dev/todomvc/#/")
#     page.get_by_role("textbox", name="What needs to be done?").click()
#     page.get_by_role("textbox", name="What needs to be done?").fill("feed the dog")
#     page.get_by_role("textbox", name="What needs to be done?").press("Enter")
#     page.get_by_role("textbox", name="What needs to be done?").fill("water the plants")
#     page.get_by_role("textbox", name="What needs to be done?").press("Enter")
#     page.get_by_role("textbox", name="What needs to be done?").fill("buy chocolates")
#     page.get_by_role("textbox", name="What needs to be done?").press("Enter")
#     page.get_by_role("listitem").filter(has_text="water the plants").get_by_label("Toggle Todo").check()
#     expect(page.get_by_text("water the plants")).to_be_visible()
#     page.get_by_role("link", name="Active").click()
#     expect(page.get_by_text("feed the dog")).to_be_visible()
#     expect(page.get_by_text("buy chocolates")).to_be_visible()
#     page.get_by_role("button", name="Clear completed").click()
#     expect(page.get_by_role("heading", name="todos")).to_be_visible()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)

