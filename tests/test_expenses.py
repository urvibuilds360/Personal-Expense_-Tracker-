import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from expense_manager import add_expense


add_expense(
    300,
    "Food",
    "Lunch",
    "29-09-2026"
)

print("Test completed successfully!")