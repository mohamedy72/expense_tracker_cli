import argparse


def cli_entry():
    parser = argparse.ArgumentParser(prog="expense")
    subparsers = parser.add_subparsers(
        title="subcommands", help="Expenses tracker", dest="action"
    )

    # Subcommand for adding a new expense
    add_action = subparsers.add_parser("add", help="Add new expense")
    add_action.add_argument(
        "--category", type=str, default="General", metavar="CATEGORY"
    )
    add_action.add_argument("--amount", type=float, default=0.0, metavar="AMOUNT")
    add_action.add_argument(
        "--description", type=str, default="", metavar="DESCRIPTION"
    )

    # Subcommand for listing all expenses
    list_action = subparsers.add_parser("list", help="List all expenses")
    list_action.add_argument(
        "--category",
        type=str,
        help="List all expenses with specific category",
        default="General",
        metavar="FILTER",
    )

    # Subcommand for the summary of all expenses
    subparsers.add_parser("summary", help="Generate total expenses")

    args = parser.parse_args()

    return args
