import logging
import os

from app.config import LOGS_OUTPUT_DIR

# Set path to log file.
log_file = os.path.join(LOGS_OUTPUT_DIR, "app.log")


def init_logger() -> None:
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO,
        datefmt="%m-%d %H-%M",
        filename=log_file,
        filemode="a",
    )
