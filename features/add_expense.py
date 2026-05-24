import random
import time


def add_expense(category, amount, desc):
    expense_id = random.randint(1, 100) * 0.5

    new_expense = {
        "id": expense_id,
        "category": category,
        "amount": amount,
        "desc": desc,
        "date": time.time(),
    }
    print("✅ Expense Created")
    return new_expense
