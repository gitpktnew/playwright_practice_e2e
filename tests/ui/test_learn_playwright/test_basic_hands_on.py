import re
import pytest
from playwright.sync_api import Page, expect
from tests.config import TestConfig
import time

# The test functions acquire new browser pages and do some testing
def test_fill_basic_form_and_submit(new_page: Page, app_config: TestConfig):
    new_page.goto(app_config.base_url)
    expect(new_page).to_have_title(re.compile("Playwright"))
