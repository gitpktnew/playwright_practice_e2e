import pytest

@pytest.mark.smoke
@pytest.mark.ui
def test_homepage_loads(page, app_config):  # 'page' comes from pytest-playwright
    page.goto(app_config.base_url, timeout=app_config.api_timeout * 1000)
    assert app_config.base_url in page.url
