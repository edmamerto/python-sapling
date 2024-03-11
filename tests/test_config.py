import os

from src.config import Settings, get_config, initialize_config


def test_get_config(monkeypatch):
    # Mock the environment variable to be unset
    monkeypatch.delenv("ENVIRONMENT", raising=False)

    # Call get_config to ensure config is initialized
    config = get_config()
    assert config is not None
    assert config.environment == "dev"


def test_initialize_config(monkeypatch, caplog):
    # Mock the environment variable to be unset
    monkeypatch.setenv("ENVIRONMENT", "prod")

    # Call initialize_config to ensure it initializes config correctly
    config = initialize_config()

    # Check if the config is an instance of Settings
    assert isinstance(config, Settings)

    # Check if environment and log_level are set correctly
    assert config.environment == "prod"
    assert config.log_level == os.getenv("LOG_LEVEL")
