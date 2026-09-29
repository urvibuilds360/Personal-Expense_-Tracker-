from database import create_table
from expense_manager import (
    add_expense,
    view_expenses,
    update_expense,
    delete_expense
)
from analysis import display_analysis
from utils import get_valid_amount, get_valid_category, get_valid_date


def add_new_expense():
    print("\n========== ADD EXPENSE ==========")

    amount = get_valid_amount()
    category = get_valid_category()

    description = input("Enter description: ")
    date = get_valid_date()

    add_expense(amount, category, description, date)


def update_existing_expense():
    print("\n========== UPDATE EXPENSE ==========")

    try:
        expense_id = int(input("Enter Expense ID to update: "))

        amount = get_valid_amount()
        category = get_valid_category()

        description = input("Enter new description: ")
        date = get_valid_date()

        update_expense(
            expense_id,
            amount,
            category,
            description,
            date
        )

    except ValueError:
        print("Please enter a valid Expense ID.")


def delete_existing_expense():
    print("\n========== DELETE EXPENSE ==========")

    try:
        expense_id = int(input("Enter Expense ID to delete: "))
        delete_expense(expense_id)

    except ValueError:
        print("Please enter a valid Expense ID.")


def main():
    create_table()

    while True:
        print("\n")
        print("======================================")
        print("       PERSONAL EXPENSE TRACKER")
        print("======================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Expense Analysis")
        print("6. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            update_existing_expense()

        elif choice == "4":
            delete_existing_expense()

        elif choice == "5":
            display_analysis()

        elif choice == "6":
            print("\nThank you for using Personal Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()