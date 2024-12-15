# dashboard.py

from transaction import Transaction
from budget import Budget
from investment import Investment
from user import User
from account import Account

class Dashboard:
    def __init__(self, user):
        self.user = user

    def show_dashboard(self, accounts, transactions, budgets, investments):
        """Display the user's financial dashboard."""
        print(f"Welcome, {self.user.name}!")
        print(f"Email: {self.user.email}")
        print(f"Current Balance: ${self.user.balance:.2f}")
        print("===========================")

        # Display Accounts
        print("Accounts:")
        for account in accounts:
            print(f"Account ID: {account.account_id}, Type: {account.account_type}, Balance: ${account.balance:.2f}")
        print("===========================")

        # Display Transactions
        print("Recent Transactions:")
        for transaction in transactions:
            transaction.display_transaction()
        
        # Display Budgets
        print("Budgets:")
        for budget in budgets:
            budget.display_budget()

        # Display Investments
        print("Investments:")
        for investment in investments:
            investment.display_investment()

    def show_menu(self, accounts, transactions, budgets, investments):
        while True:
            print("\nMenu:")
            print("1. View Accounts")
            print("2. View Transactions")
            print("3. View Budgets")
            print("4. View Investments")
            print("5. Exit")
            
            choice = input("Select an option: ")
            
            if choice == '1':
                self.show_accounts(accounts)
            elif choice == '2':
                self.show_transactions(transactions)
            elif choice == '3':
                self.show_budgets(budgets)
            elif choice == '4':
                self.show_investments(investments)
            elif choice == '5':
                print("Exiting dashboard.")
                break
            else:
                print("Invalid choice. Please try again.")

    def show_accounts(self, accounts):
        print("Accounts:")
        for account in accounts:
            print(f"Account ID: {account.account_id}, Type: {account.account_type}, Balance: ${account.balance:.2f}")

    def show_transactions(self, transactions):
        print("Recent Transactions:")
        for transaction in transactions:
            transaction.display_transaction()

    def show_budgets(self, budgets):
        print("Budgets:")
        for budget in budgets:
            budget.display_budget()

    def show_investments(self, investments):
        print("Investments:")
        for investment in investments:
            investment.display_investment()

# Example usage
if __name__ == "__main__":
    # Create a user
    user = User(user_id=1, name="John Doe", email="john@example.com", password="securepassword")
    
    # Create accounts
    account1 = Account(account_id=1, account_type="Savings", balance=1000.00, user_id=user.user_id)
    account2 = Account(account_id=2, account_type="Checking", balance=500.00, user_id=user.user_id)

    # Create transactions
    transactions = [
        Transaction(transaction_id=1, amount=200.00, transaction_type="Deposit", date="2023-10-01", account_id=account1.account_id),
        Transaction(transaction_id=2, amount=150.00, transaction_type="Withdrawal", date="2023-10-02", account_id=account1.account_id),
    ]

    # Create budgets
    budgets = [
        Budget(budget_id=1, user_id=user.user_id, category="Groceries", amount=300.00, start_date="2023-10-01", end_date="2023-10-31"),
    ]

    # Create investments
    investments = [
        Investment(investment_id=1, user_id=user.user_id, investment_type="Stocks", amount=1000.00, date="2023-10-01", return_rate=8.0),
    ]

    # Create a dashboard and show it
    dashboard = Dashboard(user)
    dashboard.show_dashboard([account1, account2], transactions, budgets, investments)