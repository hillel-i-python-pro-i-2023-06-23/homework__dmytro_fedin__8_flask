import io
import pandas as pd

from application.services.responses import get_response

# Set urls to process.
drive_url = (
    "https://drive.google.com/file/d/13nk_FYpcayUck2Ctrela5Tjt9JQbjznt/view"
)
csv_url_pattern = "https://drive.google.com/uc?export=download&id=FILE_ID"


def extract_file_id(url: str) -> str | None:
    search_start = url.find("/d/") + 3
    search_end = url.find("/view")

    if search_start != -1 and search_end != -1:
        return url[search_start:search_end]
    else:
        return None


def build_file_link(some_id: str, some_url: str) -> str | None:
    file_id = some_id

    if file_id:
        return some_url.replace("FILE_ID", file_id)
    else:
        return None


def get_csv_content() -> bytes | None:
    current_id = extract_file_id(drive_url)

    current_link = build_file_link(current_id, csv_url_pattern)
    csv_url = current_link
    response = get_response(csv_url)

    if response.status_code == 200:
        csv_content = response.content

        return csv_content
    else:
        return None


def read_csv_content() -> pd.DataFrame:
    content = get_csv_content()
    file_obj = io.BytesIO(content)

    data_frame = pd.read_csv(file_obj)

    return data_frame
