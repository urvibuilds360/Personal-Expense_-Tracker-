from database import get_connection, create_table


def get_total_expense():
    create_table()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")

    result = cursor.fetchone()[0]

    connection.close()

    if result is None:
        return 0

    return result


def get_category_summary():
    create_table()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)

    results = cursor.fetchall()

    connection.close()

    return results


def get_highest_expense():
    create_table()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM expenses
        ORDER BY amount DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    connection.close()

    return result


def display_analysis():
    print("\n========== EXPENSE ANALYSIS ==========")

    total = get_total_expense()
    print("Total Expense: ₹", total)

    print("\nCategory-wise Spending:")

    categories = get_category_summary()

    if not categories:
        print("No expenses found.")
    else:
        for category, amount in categories:
            print(category, ": ₹", amount)

    highest = get_highest_expense()

    if highest:
        print("\nHighest Expense:")
        print("Amount: ₹", highest[1])
        print("Category:", highest[2])
        print("Description:", highest[3])
        print("Date:", highest[4])
        