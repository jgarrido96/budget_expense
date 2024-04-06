

class BudgetCategory:

    def __init__(self):
        self.__budget_category = ""
        self.__budget = 0
        self.__budget_category_list = []
        self.__expenses_category = ""
        self.__expense = 0
        self.__expense_category_list = []


    def get_budget_category(self):
        return self.__budget_category, self.__budget
    
    def get_expense_category(self):
        return self.__expenses_category, self.__expense

    def set_budget_category(self):
        print("\nLet's add some budget categories!")
        while True:
            category_input = input("Name of category (type 'done' when finished): ")
            if category_input == 'done':
                print("\nReturning...")
                break
            else:
                budget_input = int(input(f"Budget for {category_input}: "))
                if isinstance(budget_input, int):
                    if budget_input > 0:
                        self.__budget = budget_input
                        self.__budget_category = category_input
                        self.__budget_category_list.append((category_input, budget_input))
                    else:
                        print("Please enter a whole number greater than 0.")
                else:
                     print("Please enter a valid number.")

    def set_expense_category(self):
        print("\nLet's add some expense categories!")
        while True:
            category_input = input("Name of category (type 'done' when finished): ")
            if category_input == 'done':
                print("\nReturning...")
                break
            else:
                expense_input = int(input(f"Expense for {category_input}: "))
                for budget in self.__budget_category_list:
                    if budget[0] == category_input:
                        if expense_input > budget[1]:
                            print(f"You didn't stay in budget for {category_input}.")
                            break
                if isinstance(expense_input, int):
                    if expense_input > 0:
                        self.__expense = expense_input
                        self.__expenses_category = category_input
                        self.__expense_category_list.append((category_input, expense_input))
                    else:
                        print("Please enter a whole number greater than 0.")
                else:
                     print("Please enter a valid number.")



    def display_category_summary(self):
        print("\nHere's how you did:\n")
        for budget in self.__budget_category_list:
            for expense in self.__expense_category_list:
                if budget[0] == expense[0]:
                    print(f"\n\tBudget for {budget[0]}: ${budget[1]}\tExpense for {expense[0]}: ${expense[1]}\tThis is your remaining budget for {budget[0]}: ${budget[1] - expense[1]}")
                else:
                    continue
        return self.__budget_category_list
