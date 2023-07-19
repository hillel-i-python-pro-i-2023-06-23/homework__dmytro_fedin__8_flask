import pathlib
from typing import Final

# Set directories to get services.
ROOT_DIR: Final[pathlib.Path] = pathlib.Path(__file__).parents[1]
FILES_INPUT_DIR: Final[pathlib.Path] = ROOT_DIR.joinpath("source")
LOGS_OUTPUT_DIR: Final[pathlib.Path] = ROOT_DIR.joinpath("logs")
FILES_OUTPUT_DIR: Final[pathlib.Path] = ROOT_DIR.joinpath("output")
