import logging

from application.loggers.init_logging import init_logger


def get_logger() -> logging.Logger:
    init_logger()
    return logging.getLogger()
