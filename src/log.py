import logging

import structlog


def configure_logging():

    logging.basicConfig(level=logging.DEBUG)

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


# Configure the logging at module import
configure_logging()


def get_logger(name=None):
    return structlog.get_logger(name)
