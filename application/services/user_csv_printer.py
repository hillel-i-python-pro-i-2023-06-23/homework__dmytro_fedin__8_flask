import pathlib
import csv

from application.services.config import FILES_OUTPUT_DIR
from application.loggers.logger import get_logger
from application.services.user_generator import generate_users, User


# Set path to csv file.
csv_file_path = FILES_OUTPUT_DIR.joinpath("users.csv")


def write_csv(amount: int = 100, file_path: pathlib.Path = None):
    logger = get_logger()

    if file_path is None:
        file_path = csv_file_path
        logger.info(
            f"csv_file_path is None. Use default value: {file_path.as_uri()}"
        )

    with open(file_path, "w", newline="") as csv_file:
        logger.info("Start getting csv file")

        csv_writer = csv.DictWriter(csv_file, fieldnames=User.get_fieldnames())
        csv_writer.writeheader()
        user_generator = generate_users(amount=amount)

        for index, user in enumerate(user_generator, start=1):
            csv_writer.writerow(user.get_dict())

    logger.info(f"End getting csv file for amount of users {amount}")
    print(f"{amount} users have been generated")
