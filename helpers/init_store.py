import json


def init_store(filepath):
    filepath.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(filepath, "w") as f:
            json.dump([], f)
        print(f"Expenses JSON store is created successfully at: {filepath}")
    except Exception as e:
        raise e
