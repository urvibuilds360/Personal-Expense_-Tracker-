from database import get_connection, create_table


def add_expense(amount, category, description, date):
    create_table()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?, ?, ?, ?)
    """, (amount, category, description, date))

    connection.commit()
    connection.close()

    print("Expense added successfully!")


def view_expenses():
    create_table()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()

    connection.close()

    if not expenses:
        print("No expenses found.")
        return

    print("\n========== ALL EXPENSES ==========")

    for expense in expenses:
        print("ID:", expense[0])
        print("Amount: ₹", expense[1])
        print("Category:", expense[2])
        print("Description:", expense[3])
        print("Date:", expense[4])
        print("----------------------------------")


def update_expense(expense_id, amount, category, description, date):
    create_table()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE expenses
        SET amount = ?, category = ?, description = ?, date = ?
        WHERE id = ?
    """, (amount, category, description, date, expense_id))

    connection.commit()

    if cursor.rowcount == 0:
        print("Expense not found.")
    else:
        print("Expense updated successfully!")

    connection.close()


def delete_expense(expense_id):
    create_table()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        print("Expense not found.")
    else:
        print("Expense deleted successfully!")

    connection.close()
    
# Temporary testing code

add_expense(500, "Education", "Notebook", "29-09-2026")

print("\nBefore Update:")
view_expenses()

update_expense(2, 600, "Education", "Programming Book", "30-09-2026")

print("\nAfter Update:")
view_expenses()

delete_expense(2)

print("\nAfter Delete:")
view_expenses()