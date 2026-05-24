from pathlib import Path
import json

CURRENT_DIR = Path.cwd()
FILE_NAME = "expenses.json"
STORE_LOCATION = Path(CURRENT_DIR) / "data" / FILE_NAME


def init_store():
    STORE_LOCATION.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(STORE_LOCATION, "w") as f:
            json.dump([], f)
        print(f"Expenses JSON store is created successfully at: {STORE_LOCATION}")
    except Exception as e:
        raise e
