from datetime import datetime

class Budget:
    def __init__(self):
        self.income = 0.0
        self.date = None
        self.budget_category = ""        # Budget category name
        self.planned_amount = 0.0        # Planned budget amount
        self.actual_spending = 0.0      # Actual spending value
        self.budgets = []                # List to store individual budget entries

    def set_date(self):
        """
        Prompt the user to enter the date they want to set the budget for.
        """
        while True:
            try:
                date_input = input("Enter the date for your budget (YYYY-MM-DD): ")
                self.date = datetime.strptime(date_input, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid format. Please enter the date in YYYY-MM-DD format.")

    def set_income(self):
        """
        Prompt the user to enter their total income.
        """
        while True:
            try:
                self.income = float(input("Enter your monthly income (RM): "))
                if self.income <= 0:
                    raise ValueError("Income must be a positive value.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}")

    def set_budget(self):
        """
        Allow the user to allocate budgets for selected categories.
        """
        print("\n-- Budget Categories --")
        categories = ["Food", "Transportation", "Utilities", "Entertainment"]
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

        self.budgets.clear()  # Clear previous budgets if re-planning

        while True:
            try:
                choice = int(input("Enter the number corresponding to the category you want to set a budget for (or 0 to finish): "))
                if choice == 0:
                    break
                if choice < 1 or choice > len(categories):
                    raise ValueError("Invalid category number.")

                category = categories[choice - 1]
                amount = float(input(f"Enter your planned budget for {category} (RM): "))
                if amount < 0:
                    raise ValueError("Budget amount cannot be negative.")

                # Store budget category, planned amount, and actual spending directly in attributes
                self.budget_category = category
                self.planned_amount = amount
                self.actual_spending = 0.0

                # Append the budget as a dictionary
                self.budgets.append({
                    "budget_category": self.budget_category,
                    "planned_amount": self.planned_amount,
                    "actual_spending": self.actual_spending
                })
            except ValueError as e:
                print(f"Invalid input: {e}")

    def enter_actual_spending(self):
        """
        Allow the user to input actual spending for each category.
        """
        print("\n-- Enter Actual Spending for Each Category --")
        for budget in self.budgets:
            while True:
                try:
                    spending = float(input(f"Enter your actual spending for {budget['budget_category']} (RM): "))
                    if spending < 0:
                        raise ValueError("Spending cannot be negative.")
                    budget["actual_spending"] = spending
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

    def check_budget(self, budget):
        """
        Check if actual spending exceeds the planned budget.
        """
        return budget["actual_spending"] <= budget["planned_amount"]

    def is_close_to_budget(self, budget, threshold=0.9):
        """
        Check if the actual spending is within a threshold of the planned budget.
        Alerts when actual spending is within a certain percentage of the planned budget.
        """
        return budget["actual_spending"] >= budget["planned_amount"] * threshold

    def review_budget(self):
        """
        Review if the actual spending is within the budget and alert if it's close to exceeding.
        """
        print("\n-- Budget Review --")
        overspending = False

        for budget in self.budgets:
            print(f"Category: {budget['budget_category']}")
            print(f"Planned Budget: RM {budget['planned_amount']:.2f}")
            print(f"Actual Spending: RM {budget['actual_spending']:.2f}")

            # Check if budget is exceeded
            if not self.check_budget(budget):
                print("Status: Overspent ❌")
                overspending = True
            else:
                print("Status: Within Budget ✅")

            # Check if spending is close to the budget (e.g., 90%)
            if self.is_close_to_budget(budget):
                print("Warning: You're close to exceeding your budget! ⚠️")
            print()

        return not overspending

    def display_summary(self):
        """
        Display a summary of the user's budgets and remaining savings.
        """
        total_planned = sum(budget["planned_amount"] for budget in self.budgets)
        total_spent = sum(budget["actual_spending"] for budget in self.budgets)
        savings = self.income - total_spent

        print("\n-- Budget Summary --")
        for budget in self.budgets:
            # Print the budget attributes (category, planned amount, actual spending) on one line
            print(f"Category: {budget['budget_category']}, Planned Amount: RM {budget['planned_amount']:.2f}, Actual Spending: RM {budget['actual_spending']:.2f}")

        print(f"Total Income: RM {self.income:.2f}")
        print(f"Total Planned Budget: RM {total_planned:.2f}")
        print(f"Total Actual Spending: RM {total_spent:.2f}")
        print(f"Remaining Savings: RM {savings:.2f}")

        if savings >= 0:
            print("Great job! You managed your budget successfully.")
        else:
            print("Warning: Your spending exceeded your income!")

    def run_budget_planning(self):
        """
        Run the entire budget planning process.
        """
        self.set_date()
        self.set_income()
        while True:
            self.set_budget()
            self.enter_actual_spending()

            # Check if any category overspent
            if self.review_budget():
                print(f"\nCongratulations! Your budget planning for the {self.date.strftime('%B')} month is successful.")
                break
            else:
                print("\nOverspending detected. Please re-plan your budget for this month.\n")


def main():
    print("-- Budget Planning System --")
    budget = Budget()
    budget.run_budget_planning()


if __name__ == "__main__":
    main()

import datetime

class FinancialGoal:
    def __init__(self):
        self.goal_month = ""
        self.goals = []
        self.achieved_month = ""  # Store the month goals are achieved

    def validate_date(self, date_str):
        """
        Validates the date in the format 'YYYY-MM'.
        """
        try:
            datetime.datetime.strptime(date_str, "%Y-%m")
            return True
        except ValueError:
            return False

    def set_months(self):
        """
        Prompt the user for the goal month, ensuring valid format.
        """
        print("\n🌟 Welcome to the Financial Goals Planner! 🌟")
        while True:
            self.goal_month = input("Enter the month you want to achieve your goal (YYYY-MM): ").strip()
            if self.validate_date(self.goal_month):
                break
            print("❌ Invalid format! Please use 'YYYY-MM'.")

    def set_goals(self):
        """
        Allow the user to set financial goals for predefined categories.
        """
        print("\n-- 🎯 Financial Goal Categories 🎯 --")
        categories = ["Food", "Transportation", "Utilities", "Entertainment"]
        selected_categories = []

        while True:
            print("\nAvailable Categories:")
            for idx, category in enumerate(categories, 1):
                if category not in selected_categories:
                    print(f"{idx}. {category}")

            choice = input("\nSelect a category number to set a goal, or type 'done' to finish: ").strip().lower()
            if choice == 'done':
                if not selected_categories:
                    print("🚨 Please set at least one financial goal!")
                    continue
                break

            try:
                idx = int(choice) - 1
                if idx < 0 or idx >= len(categories) or categories[idx] in selected_categories:
                    print("⚠️ Invalid selection. Please choose an available category.")
                    continue

                category = categories[idx]

                # Enter the purpose for this category
                purpose = input(f"Enter the purpose for saving in {category}: ").strip()

                # Enter the savings goal amount
                while True:
                    try:
                        amount = float(input(f"Enter your savings goal for {category} (RM): "))
                        if amount <= 0:
                            raise ValueError("Savings amount must be a positive value.")
                        self.goals.append({
                            "category": category,
                            "purpose": purpose,
                            "goal_amount": amount,
                            "current_savings": 0.0
                        })
                        selected_categories.append(category)
                        break
                    except ValueError as e:
                        print(f"❌ Invalid input: {e}")

            except ValueError:
                print("⚠️ Invalid input. Please enter a valid number or 'done'.")

    def add_savings_to_goals(self):
        """
        Allow the user to add savings for each goal and check progress.
        """
        print("\n-- 💰 Add Savings to Your Goals 💰 --")
        for goal in self.goals:
            while True:
                try:
                    print(f"\nCategory: {goal['category']}")
                    print(f"Purpose: {goal['purpose']}")
                    print(f"Goal Amount: RM {goal['goal_amount']:.2f}")
                    print(f"Current Savings: RM {goal['current_savings']:.2f}")

                    amount = float(input(f"Enter the amount to add to your savings for {goal['category']} (RM): "))
                    if amount < 0:
                        raise ValueError("Savings amount cannot be negative.")

                    goal['current_savings'] += amount
                    if goal['current_savings'] >= goal['goal_amount']:
                        print(f"Congratulations!🎉 You've reached your savings goal for {goal['category']} before {self.goal_month}!🏆")
                    else:
                        print(f"📈 Current Savings for {goal['category']}: RM {goal['current_savings']:.2f} (Goal: RM {goal['goal_amount']:.2f})")
                    break
                except ValueError as e:
                    print(f"❌ Invalid input: {e}")

    def display_goals(self):
        """
        Display a summary of the user's financial goals and progress.
        """
        print("\n-- 📊 Financial Goals Summary 📊 --")
        print(f"\n{'Category':<15}{'Purpose':<20}{'Goal Amount':<15}{'Current Savings':<20}{'Status':<15}")
        print("-" * 85)
        for goal in self.goals:
            status = "✅ Goal Reached!" if goal['current_savings'] >= goal['goal_amount'] else "⏳ In Progress"
            print(f"{goal['category']:<15}{goal['purpose']:<20}RM {goal['goal_amount']:<13.2f}RM {goal['current_savings']:<18.2f}{status:<15}")

    def run_financial_goals(self):
        """
        Run the entire financial goals planning process.
        """
        self.set_months()
        self.set_goals()
        while True:
            self.add_savings_to_goals()
            self.display_goals()

            # Ask if the user wants to continue
            continue_choice = input("\n💭 Do you want to add more savings? (yes/no): ").strip().lower()
            if continue_choice != 'yes':
                # Convert the goal month to a full month name
                achieved_month_name = datetime.datetime.strptime(self.goal_month, "%Y-%m").strftime("%B")
                print(f"\nThank you for using the Financial Goals Planner!🙏 Have a great day!🌟\nGoals set to achieve by {achieved_month_name} {self.goal_month[:4]}.")
                break


def main():
    planner = FinancialGoal()
    planner.run_financial_goals()


if __name__ == "__main__":
    main()
