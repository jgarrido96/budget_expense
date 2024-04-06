

class BudgetCategory:
    # Constructor and private attributes
    # ...
    def __init__(self):
        self.__budget_category = "" # private attribute
        self.__budget = 0 # private attribute
        self.__budget_category_list = []
        self.__expenses_category = ""
        self.__expense = 0
        self.__expense_category_list = []


    # setter for category and budget
    # def set_category(self, category, budget):
    #     self.__category = category
    #     self.__budget = budget

    # Getters and setters for category name and budget
    # ...
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
        # Method to display the budget category details
        # ...
        print("Here's how you did:\n")
        for budget in self.__budget_category_list:
            for expense in self.__expense_category_list:
                if budget[0] == expense[0]:
                    print(f"\t\nBudget for {budget[0]}: ${budget[1]}\tExpense for {expense[0]}: ${expense[1]}\tThis is your remaining budget for {budget[0]}: ${budget[1] - expense[1]}")
                else:
                    print(f"You didn't spend on {budget[0]}, so your budget of ${budget[1]} remains the same.")
                    print(f"You didn't plan on {expense[0]} and spent ${expense[1]}.")
        return self.__budget_category_list


# print("Welcome to the Budget Palooza! Balance your budgets and expenses!")

# first_category = input("Let's enter your first category to get started! ")
# first_budget = int(input("Next, what is your budget for this? "))

# # Defined first category of food. 
# food_category = BudgetCategory(first_category, first_budget)

# # food_category.add_expense(100)
# # prints default category
# # print(f"This is a default category:\n{food_category.get_category()}")
# print('\n')
# add_input = input("Would you like to add another category? y/n ")
# if add_input == 'n':
#     pass
# if add_input == 'y':
#     food_category.set_category()

# # print(food_category.display_category_summary())
# # prints the last category and budget entered
# print(f"Last category entered: {food_category.get_category()}")
# final_list = food_category.display_category_summary()

# # prints list of tuples of all categories and budgets
# print(f"\nHere is what you added today:")
# print(f"\nCategory:\tBudget:\n")
# for category in final_list:
#     print(f"{category[0]}\t\t{category[1]}")

