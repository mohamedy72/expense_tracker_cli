import json


def save_expenses(expenses, file):
    with open(file, "w") as f:
        json.dump(expenses, f)

    print("Expense Saved to your store")
