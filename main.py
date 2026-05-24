from pathlib import Path
from cli import cli_entry
from features import add_expense, list_expenses
from helpers import init_store, save_expenses, load_expenses

CURRENT_DIR = Path.cwd()
FILE_NAME = "expenses.json"
STORE_LOCATION = Path(CURRENT_DIR) / "data" / FILE_NAME


def main():
    expenses = []
    if Path(Path.cwd() / "data" / "expenses.json").exists():
        print("✅ Store already intialized. ")
        print("⏳ Loading saved expenses instead")
        expenses = load_expenses(STORE_LOCATION)
    else:
        print("⌛ Initializing the store for the first time")
        init_store(STORE_LOCATION)

    arguments = cli_entry()

    if arguments.action == "add":
        new_exp = add_expense(
            arguments.category, arguments.amount, arguments.description
        )
        expenses.append(new_exp)
        save_expenses(expenses, STORE_LOCATION)
    elif arguments.action == "list":
        print(arguments)
        if arguments.category:
            list_expenses(expenses, arguments.category)
        else:
            list_expenses(expenses)


if __name__ == "__main__":
    main()
