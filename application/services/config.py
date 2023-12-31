from pathlib import Path

# Set directories to get services.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
FILES_INPUT_DIR = BASE_DIR.joinpath("source")
LOGS_OUTPUT_DIR = BASE_DIR.joinpath("logs")
FILES_OUTPUT_DIR = BASE_DIR.joinpath("output")

# For current job
FILES_DB_DIR = BASE_DIR
DB_PATH = BASE_DIR.joinpath("db", "db.sqlite")
