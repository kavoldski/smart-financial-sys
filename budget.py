# account.py

class Account:
    def __init__(self, account_id, account_type, balance, user_id):
        self.account_id = account_id
        self.account_type = account_type
        self.balance = balance
        self.user_id = user_id

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} to account ID {self.account_id}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f} from account ID {self.account_id}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def transfer(self, amount, target_account):
        """Transfer money to another account."""
        if amount > 0:
            if amount <= self.balance:
                self.withdraw(amount)  # Withdraw from this account
                target_account.deposit(amount)  # Deposit to the target account
                print(f"Transferred ${amount:.2f} from account ID {self.account_id} to account ID {target_account.account_id}.")
            else:
                print("Insufficient funds for this transfer.")
        else:
            print("Transfer amount must be positive.")

    def get_balance(self):
        """Return the current balance of the account."""
        return self.balance

# Example usage
if __name__ == "__main__":
    # Create an account instance for testing
    account1 = Account(account_id=1, account_type="Savings", balance=1000.00, user_id=1)
    account2 = Account(account_id=2, account_type="Checking", balance=500.00, user_id=1)

    # Test deposit
    account1.deposit(200.00)

    # Test withdrawal
    account1.withdraw(150.00)

    # Test transfer
    account1.transfer(100.00, account2)

    # Check balances
    print(f"Account 1 Balance: ${account1.get_balance():.2f}")
    print(f"Account 2 Balance: ${account2.get_balance():.2f}")