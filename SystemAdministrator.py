from account import Account
from user import User


class SystemAdministrator:
    def __init__(self, admin_id, name, email):
        self.admin_id = admin_id
        self.name = name
        self.email = email

    def manage_user(self, user, action):
        """Manage user accounts (e.g., activate, deactivate, update)."""
        if action == "activate":
            print(f"Activating user: {user.name}")
            # Code to activate the user
        elif action == "deactivate":
            print(f"Deactivating user: {user.name}")
            # Code to deactivate the user
        elif action == "update":
            print(f"Updating user: {user.name}")
            # Code to update user information
        else:
            print("Invalid action for user management.")

    def manage_account(self, account, action):
        """Manage accounts (e.g., add, remove, update)."""
        if action == "add":
            print(f"Adding account: {account.account_id}")
            # Code to add the account
        elif action == "remove":
            print(f"Removing account: {account.account_id}")
            # Code to remove the account
        elif action == "update":
            print(f"Updating account: {account.account_id}")
            # Code to update account information
        else:
            print("Invalid action for account management.")

    def view_reports(self, reports):
        """View various reports (e.g., user activity, financial reports)."""
        for report in reports:
            print(report)

    def provide_help(self, query):
        """Provide help desk support for user queries."""
        print(f"Help Desk Query: {query}")
        # Code to handle the query and provide assistance

# Example usage
if __name__ == "__main__":
    admin = SystemAdministrator(admin_id=1, name="Admin User", email="admin@example.com")
    
    # Example user and account management
    user = User(user_id=1, name="John Doe", email="john@example.com", password="securepassword")
    account = Account(account_id=1, account_type="Savings", balance=1000.00, user_id=user.user_id)

    admin.manage_user(user, "activate")
    admin.manage_account(account, "update")
    
    # Example help desk support
    admin.provide_help("How do I reset my password?")