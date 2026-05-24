import json


def load_expenses(file):
    try:
        # comment: Load expenses JSON file if exists
        with open(file, "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []
    # end try
    return expenses
