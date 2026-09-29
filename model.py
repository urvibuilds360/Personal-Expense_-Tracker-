class Expense:
    def __init__(self, expense_id, amount, category, description, date):
        self.expense_id = expense_id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def display(self):
        print("Expense ID:", self.expense_id)
        print("Amount: ₹", self.amount)
        print("Category:", self.category)
        print("Description:", self.description)
        print("Date:", self.date)


