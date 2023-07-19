import os.path
from application.services.config import FILES_INPUT_DIR
from application.loggers.logger import get_logger


def print_output(file_name) -> None:
    file_path = os.path.join(FILES_INPUT_DIR, file_name)

    logger = get_logger()

    def get_content() -> str:
        if os.path.isfile(file_path):
            with open(file_path) as file:
                logger.info(f"Start reading file {file_name}")

                content = file.read()
                return content
        else:
            message = f"{FILES_INPUT_DIR} folder read but no such file as {file_name} found"
            logger.info(message)
            return message

    content_to_print = get_content()
    logger.info(f"End reading file {file_name}")

    print(content_to_print)

    logger.info(f"File {file_name} printed.")
