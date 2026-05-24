import json


def save_expenses(expenses, file):
    with open(file, "w") as f:
        json.dump(expenses, f)

    print("Expenses Saved to your machine")
