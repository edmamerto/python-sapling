import logging
from unittest.mock import MagicMock

import pytest
import structlog

from src.log import configure_logging, get_logger


@pytest.fixture(autouse=True)
def configure_logging_mock(mocker):
    mocker.patch("logging.basicConfig")
    mocker.patch("structlog.configure")


def test_configure_logging():
    configure_logging()

    # Ensure logging.basicConfig is called with the correct arguments
    logging.basicConfig.assert_called_once_with(level=logging.DEBUG)

    # Ensure structlog.configure is called
    structlog.configure.assert_called_once()


def test_get_logger(mocker):
    # Mock the structlog.get_logger function
    logger_mock = MagicMock()
    mocker.patch("structlog.get_logger", return_value=logger_mock)

    # Call the get_logger function
    get_logger("test_logger")

    # Ensure structlog.get_logger is called with the correct arguments
    structlog.get_logger.assert_called_once_with("test_logger")
