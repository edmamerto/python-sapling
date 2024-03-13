import structlog


def get_logger(name=None):
    return structlog.get_logger(name)
