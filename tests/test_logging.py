import json
import logging

import pytest

from src.config import initialize_config
from src.log import get_logger


@pytest.fixture(autouse=True)
def initialize_configuration():
    initialize_config()


def test_get_logger(caplog):
    with caplog.at_level(logging.DEBUG):
        # Call get_logger to get a logger instance
        logger = get_logger()

        # Log a test message
        logger.info("Test message")

    # Assert if "Test message" is in captured logs
    assert "Test message" in caplog.text

    log = json.loads(caplog.records[-1].message)

    # Optionally, if you need to check the log-level
    assert log["event"] == "Test message"
    assert log["level"].upper() == "INFO"
