# investment.py

class Investment:
    def __init__(self, investment_id, user_id, investment_type, amount, date, return_rate):
        self.investment_id = investment_id
        self.user_id = user_id
        self.investment_type = investment_type  # e.g., "Stocks", "Bonds", "Real Estate"
        self.amount = amount  # Amount invested
        self.date = date  # Date of the investment
        self.return_rate = return_rate  # Expected return rate (as a percentage)
        self.current_value = amount  # Current value of the investment

    def calculate_return(self):
        """Calculate the expected return on the investment."""
        return self.current_value * (self.return_rate / 100)

    def update_value(self, new_value):
        """Update the current value of the investment."""
        if new_value >= 0:
            self.current_value = new_value
            print(f"Updated current value of investment ID {self.investment_id} to ${self.current_value:.2f}.")
        else:
            print("New value must be non-negative.")

    def display_investment(self):
        """Display the details of the investment."""
        print(f"Investment ID: {self.investment_id}")
        print(f"User  ID: {self.user_id}")
        print(f"Type: {self.investment_type}")
        print(f"Amount Invested: ${self.amount:.2f}")
        print(f"Date: {self.date}")
        print(f"Expected Return Rate: {self.return_rate:.2f}%")
        print(f"Current Value: ${self.current_value:.2f}")
        print(f"Expected Return: ${self.calculate_return():.2f}")
        print("===========================")

# Example usage
if __name__ == "__main__":
    # Create an investment instance for testing
    investment1 = Investment(investment_id=1, user_id=1, investment_type="Stocks", amount=1000.00, date="2023-10-01", return_rate=8.0)

    # Display investment details
    investment1.display_investment()

    # Update the current value of the investment
    investment1.update_value(1200.00)

    # Display updated investment details
    investment1.display_investment()