# budget.py
class Budget:
    def __init__(self):
        self.categories = {}  # Dictionary to hold category names and their budget limits
        self.expenses = {}    # Dictionary to hold category names and their expenses

    def add_category(self, category_name, limit):
        """Add a new budget category with a specified limit."""
        self.categories[category_name] = limit
        self.expenses[category_name] = 0  # Initialize expenses for the category

    def add_expense(self, category_name, amount):
        """Add an expense to a specified category."""
        if category_name not in self.categories:
            raise ValueError(f"Category '{category_name}' does not exist.")
        
        if amount < 0:
            raise ValueError("Expense amount must be positive.")
        
        self.expenses[category_name] += amount

    def check_budget(self, category_name):
        """Check if the expenses in a category exceed the budget limit."""
        if category_name not in self.categories:
            raise ValueError(f"Category '{category_name}' does not exist.")
        
        return self.expenses[category_name] <= self.categories[category_name]

    def get_budget_report(self):
        """Generate a report of the budget status for all categories."""
        report = {}
        for category in self.categories:
            report[category] = {
                "limit": self.categories[category],
                "spent": self.expenses[category],
                "remaining": self.categories[category] - self.expenses[category],
                "within_budget": self.check_budget(category)
            }
        return report

    def __str__(self):
        """String representation of the budget."""
        return "\n".join(f"{category}: Limit = {self.categories[category]}, Spent = {self.expenses[category]}" for category in self.categories)