
from budget_category import BudgetCategory

# from expense_category import ExpenseCategory

print("\nWelcome to the Budget Palooza! Balance your budgets and expenses!")

# start by adding Budgets
budget_list = BudgetCategory()

print('\n')
while True:
    add_input = input("Would you like to add a category? y/n ")
    if add_input == 'n':
        break
    elif add_input == 'y':
        budget_list.set_budget_category()
        budget_list.set_expense_category()
        budget_list.display_category_summary()
        break
    else:
        print("\nPlease enter a valid input.\n")
    
# expense_category = input("Now, let's add an expense! First, what was the expense on? ")
# expense_money = input("How much did that cost? ")



# expense_list = ExpenseCategory()
# while True:
#     add_input = input('\nWould you like to add an expense? y/n ')
#     if add_input == 'n':
#         break
#     elif add_input == 'y':
#         expense_list.set_expense()
#         expense_list.display_expense_summary()
#         break
#     else:
#         print("\nPlease enter a valid input.\n")






























# prints list of tuples of all categories and budgets
# print(f"\nHere is what you added today:")
# print(f"\nCategory:\tBudget:\n")
# for category in final_list:
#     print(f"{category[0]}\t\t{category[1]}")


# print("Welcome to the Budget Palooza! Balance your budgets and expenses!")
# from budget_category import BudgetCategory

# # Defined first category of food. 
# food_category = BudgetCategory("Food", 500)

# # food_category.add_expense(100)
# # prints default category
# # print(f"This is a default category:\n{food_category.get_category()}")
# print('\n')
# food_category.set_category()

# # print(food_category.display_category_summary())
# # prints the last category and budget entered
# print(f"Last category entered: {food_category.get_category()}")
# final_list = food_category.display_category_summary()

# # prints list of tuples of all categories and budgets
# print(f"\nHere is what you added today!")
# print(f"\nCategory\tBudget")
# for category in final_list:
#     print(f"{category[0]}\t\t{category[1]}")
