import pytest
import requests
from tests.config import TestConfig, config

@pytest.fixture(scope="session")
def app_config() -> TestConfig:
    """Provides immutable global test settings across the entire test session."""
    return config

@pytest.fixture(scope="session")
def api_session(app_config: TestConfig) -> requests.Session:
    """Reusable HTTP session pre-configured with shared headers."""
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})
    yield session
    session.close()
