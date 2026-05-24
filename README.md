## 💴 Expense Tracker CLI
Track your daily expenses from the terminal. Add, list, and summarize spending by category.

---
### Motivation
This is considered my first project using Python. I'm currently learning to become an AI Developer so i thought starting with a simple CLI tool is my first mile to the 1000's

---
### What I learned
The hard part about this projcet isnt functionality, I intentionally made the project hard by:
- Making sure each feature has its own git branch which enabled practicing branching, merging and managing pull requests
- Applying Separation of Concern or (SOC) and Single Responsbility functions 
- Separting each part of the app into layers espically mangaing expesnses layer so it can easily be integrated into another type of application (API, GUI .. etc)

---
### Installation
```
git clone github.com/you/cli-expense-tracker
cd cli-expense-tracker
uv venv
source .venv/bin/activate
uv sync
```

---
### Usage exmples
1. Adding new expense
`uv run main.py add --category transport --amount 30 --description "uber ride"`

2. Listing all expenses
`uv run main.py list`

3. Get an overview of all use cases
`uv run main.py --help`

----
### Project Structure
`cli/`       — CLI layer
`features/`  — Business logic
`helpers/`   — Helper function for dealing with Storage
main.py      — Entry point

---
### What's next
I have a list of tasks and functionalities to implement so I'll visit this occasionally 