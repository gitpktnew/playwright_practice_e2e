import json
import os
from dataclasses import asdict, dataclass
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(override=False)

@dataclass(frozen=True)
class TestConfig:
    env: str
    base_url: str
    api_url: str
    api_timeout: int
    headless: bool

def load_config() -> TestConfig:
    env_name = os.getenv("TEST_ENV", "staging").lower()
    
    # Load static, non-secret environment defaults from JSON
    json_path = Path(__file__).parent / "data" / "environments.json"
    with json_path.open("r", encoding="utf-8") as f:
        env_data = json.load(f)[env_name]

    # Allow CI/CD or .env to override individual URLs (e.g., from Terraform output)
    return TestConfig(
        env=env_name,
        base_url=os.getenv("BASE_URL", env_data["base_url"]).rstrip("/"),
        api_url=os.getenv("API_URL", env_data["api_url"]).rstrip("/"),
        api_timeout=int(os.getenv("API_TIMEOUT", env_data.get("api_timeout", 30))),
        headless=os.getenv("HEADLESS", "true").lower() == "true",
    )

config = load_config()
