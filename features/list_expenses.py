def list_expenses(expenses, category: None = None):

    for i, exp in enumerate(expenses, 1):
        if category:
            if exp["category"] == category:
                print(("Category: " + " " * 5), exp["category"])
                print(("Amount: " + " " * 5), exp["amount"])
                print(("Description: " + " " * 5), exp["desc"])
                print("*" * 50)
        else:
            print("# " * 15 + "💴" + "Expense: " + str(i) + "💴" + " #" * 15)
            print(("Category: " + " " * 5), exp["category"])
            print(("Amount: " + " " * 5), exp["amount"])
            print(("Description: " + " " * 5), exp["desc"])
            print("#" * 50)
