# budget.py
class Budget:
    def __init__(self, budget_id, user_id, category, amount, start_date, end_date):
        self.budget_id = budget_id
        self.user_id = user_id
        self.category = category
        self.amount = amount
        self.start_date = start_date
        self.end_date = end_date
        self.expenses = 0  # Initialize expenses for the budget

    def add_expense(self, amount):
        """Add an expense to the budget."""
        if amount < 0:
            raise ValueError("Expense amount must be positive.")
        self.expenses += amount

    def check_budget(self):
        """Check if the expenses exceed the budget limit."""
        return self.expenses <= self.amount

    def get_budget_report(self):
        """Generate a report of the budget status."""
        return {
            "category": self.category,
            "limit": self.amount,
            "spent": self.expenses,
            "remaining": self.amount - self.expenses,
            "within_budget": self.check_budget()
        }

    def __str__(self):
        """String representation of the budget."""
        return f"{self.category}: Limit = {self.amount}, Spent = {self.expenses}"