import os
import requests
from requests import Response

from urllib.parse import urlsplit
from application.loggers.logger import get_logger


def get_filename_from_url(url=None) -> str | None:
    if url is None:
        return None

    urlpath = urlsplit(url).path
    file_name = os.path.basename(urlpath)
    return file_name


def get_response(url: str) -> Response | None:
    # file_name = get_filename_from_url(url)

    logger = get_logger()

    try:
        request = requests.get(url)
        logger.info(f"Request successful in {url}")

        return request

    except requests.exceptions.RequestException as exception:
        logger.error(f"Error: {exception}")

        return None
