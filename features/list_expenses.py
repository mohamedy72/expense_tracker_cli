def list_expenses(expenses):
    for i, exp in enumerate(expenses, 1):
        print("# " * 15 + "💴" + "Expense: " + str(i) + "💴" + " #" * 15)
        print(("Category: " + " " * 5), exp["category"])
        print(("Amount: " + " " * 5), exp["amount"])
        print(("Description: " + " " * 5), exp["desc"])
        print("#" * 50)
