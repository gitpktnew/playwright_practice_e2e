import pytest

@pytest.mark.smoke
@pytest.mark.api
def test_api_health_check(api_session, app_config):
    response = api_session.get(
        f"{app_config.api_url}/health",
        timeout=app_config.api_timeout,
    )
    assert response.status_code == 404

