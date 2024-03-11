import logging
import os
from typing import Optional

import structlog
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    environment: str = "dev"
    # Default log level set to 'INFO' to reduce noise in production;
    # Also Debug-level logs contain more details that we want to avoid leaking.
    log_level: str = "INFO"


# Global variable to store the configuration
config: Optional[Settings] = None


def get_config() -> Settings:
    global config
    if config is None:
        config = initialize_config()
    return config


def initialize_config() -> Settings:
    global config
    config = Settings()
    # Default to 'dev' if ENVIRONMENT is not set
    env = os.environ.get("ENVIRONMENT", "dev")
    config.environment = env

    if env == "prod":
        dotenv_path = ".prod.env"
    else:
        dotenv_path = ".dev.env"

    load_dotenv(dotenv_path)

    # Set configuration variables
    config.log_level = os.getenv("LOG_LEVEL", "INFO")
    # Add other configuration variables as needed

    logging.basicConfig(level=config.log_level)

    structlog.configure(
        processors=[
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="iso", key="timestamp_utc"),
            structlog.processors.JSONRenderer(indent=2, sort_keys=True),
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    logging.debug("Initialized configuration: %s", config)
    return config
