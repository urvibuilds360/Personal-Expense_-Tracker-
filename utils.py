def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: ₹ "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid number.")


def get_valid_category():
    categories = [
        "Food",
        "Transport",
        "Education",
        "Shopping",
        "Entertainment",
        "Other"
    ]

    while True:
        print("\nCategories:")
        
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        choice = input("Choose a category: ")

        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            return categories[int(choice) - 1]

        print("Please choose a valid category.")


def get_valid_date():
    while True:
        date = input("Enter date (DD-MM-YYYY): ")

        parts = date.split("-")

        if len(parts) == 3 and all(part.isdigit() for part in parts):
            if len(parts[0]) == 2 and len(parts[1]) == 2 and len(parts[2]) == 4:
                return date

        print("Please enter the date in DD-MM-YYYY format.")