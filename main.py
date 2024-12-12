# main.py
from user import User
from account import Account
from transaction import Transaction
from budget import Budget
from investment import Investment
from dashboard import Dashboard

# Example usage
if __name__ == "__main__":
    user = User(user_id=1, name="John Doe", email="john@example.com", password="securepassword")
    user.balance = 1500.00  # Example balance

    # Create some example accounts, transactions, budgets, and investments
    accounts = [Account(account_id=1, account_type="Savings", balance=1000.00, user_id=user.user_id)]
    transactions = [Transaction(transaction_id=1, amount=100.00, transaction_type="Deposit", date="2023-10-01", account_id=1)]
    budgets = [Budget(budget_id=1, user_id=user.user_id, category="Groceries", amount=300.00, start_date="2023-10-01", end_date="2023-10-31")]
    investments = [Investment(investment_id=1, user_id=user.user_id, investment_type="Stocks", amount=200.00, date="2023-10-01")]

    # Create a dashboard and show it
    dashboard = Dashboard(user)
    dashboard.show_dashboard(accounts, transactions, budgets, investments)