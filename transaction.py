# transaction.py
class Transaction:
    def __init__(self, transaction_id, amount, transaction_type, date, account_id):
        self.transaction_id = transaction_id
        self.amount = amountgithub
        self.transaction_type = transaction_type  # e.g., "Deposit", "Withdrawal"
        self.date = date  # Format: "YYYY-MM-DD"
        self.account_id = account_id

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Type: {self.transaction_type}, Amount: ${self.amount:.2f}, Date: {self.date}, Account ID: {self.account_id}"

    def display_transaction(self):
        """Display the transaction details."""
        print(self)  # This will call the __str__ method

    def is_deposit(self):
        return self.transaction_type.lower() == "deposit"

    def is_withdrawal(self):
        return self.transaction_type.lower() == "withdrawal"

    def get_transaction_details(self):
        return {
            "transaction_id": self.transaction_id,
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "date": self.date,
            "account_id": self.account_id
        } #still not working