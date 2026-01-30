# Expense Tracker & Budget Manager

Expenses = []   # empty list
monthly_budget = 0 


class Expense:


    # method 1: constructor
    def __init__(self, amount, category, note, date):
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date


    # method 2: print expense
    def __str__(self):
        return f'{self.amount} | {self.category} | {self.note} | {self.date}'


while True:


    # Menu
    print()
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Expense")
    print("4. View Spending by Category")
    print("5. Set Monthly Budget")
    print("6. Check Budget Status")
    print("7. Exit")
    print()


    user_menu_number = int(input("Enter a Number: "))
    print()


    # 1. Add Expense
    if user_menu_number == 1:
        amount = int(input("Enter Amount: "))
        category = input("Enter Category: ")
        note = input("Enter Note: ")
        date = input("Enter Date: ")

        expense = Expense(amount, category, note, date)  
        Expenses.append(expense)
        print("Expense added!\n")


    # 2. View All Expense
    elif user_menu_number == 2:
        for exp in Expenses:
            print(exp)
        print()


    # 3. View Total Spending
    elif user_menu_number == 3:
        total = sum(exp.amount for exp in Expenses)   
        print("Total Expenses:", total)
        print()


    # 4. View Spending by Category
    elif user_menu_number == 4:
        if not Expenses:
            print("No expenses recorded.\n")
        else:
            category_totals = {}

            for exp in Expenses:
                if exp.category in category_totals:
                    category_totals[exp.category] += exp.amount
                else:
                    category_totals[exp.category] = exp.amount

            print("Spending by Category:")
            for cat, amt in category_totals.items():
                print(cat, ":", amt)
            print()


    # 5. Set Monthly Budget
    elif user_menu_number == 5:
        budget_input = int(input("Enter Monthly Budget: "))
        if budget_input > 0:
            monthly_budget = budget_input
            print("Budget set successfully!\n")
        else:
            print("Budget must be greater than 0!\n")


    # 6. Check Budget Status
    elif user_menu_number == 6:
        if monthly_budget == 0:
            print("Monthly budget not set yet.\n")
        else:
            total_spent = sum(exp.amount for exp in Expenses)
            remaining = monthly_budget - total_spent

            print("Budget:", monthly_budget)
            print("Total Spent:", total_spent)

            if remaining > 0:
                print("Remaining Budget:", remaining, "\n")
            elif remaining == 0:
                print("You have exactly used your budget!\n")
            else:
                print("⚠ Budget Exceeded by:", abs(remaining), "\n")


    # 7. Exit
    elif user_menu_number == 7:
        print("Exiting program")
        break
