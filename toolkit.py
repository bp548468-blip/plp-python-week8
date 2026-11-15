# Personal Mini-Toolkit - Week 8 Final Project
# Tools: 1) Calculator  2) To-Do List  3) Expense Tracker
# Uses: variables, input/output, conditionals, loops, lists

# Lists to store data that changes while program runs
todos = []
expenses = []

def show_menu():
    print("\n===== PERSONAL MINI-TOOLKIT =====")
    print("1. Quick Calculator")
    print("2. To-Do List Manager")
    print("3. Expense Tracker")
    print("4. Quit")
    print("=================================")

# Tool 1: Calculator - uses conditionals and f-strings
def calculator():
    print("\n--- Quick Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Choose: +  -  *  /")
        op = input("Enter operation: ")

        if op == "+":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif op == "-":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif op == "*":
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif op == "/":
            if num2 == 0:
                print("Oops! You cannot divide by zero.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid operation. Please use + - * /")
    except ValueError:
        print("Please enter numbers only.")

# Tool 2: To-Do List - uses a list that changes + loop + conditionals
def todo_manager():
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Back to main menu")
        choice = input("Choose (1-4): ")

        if choice == "1":
            task = input("Enter new task: ")
            todos.append(task)
            print(f"Added: {task}")
        elif choice == "2":
            if len(todos) == 0:
                print("Your to-do list is empty.")
            else:
                print("Your tasks:")
                for i, task in enumerate(todos, start=1):
                    print(f"{i}. {task}")
        elif choice == "3":
            if len(todos) == 0:
                print("Nothing to remove.")
            else:
                for i, task in enumerate(todos, start=1):
                    print(f"{i}. {task}")
                try:
                    num = int(input("Enter task number to remove: "))
                    if 1 <= num <= len(todos):
                        removed = todos.pop(num - 1)
                        print(f"Removed: {removed}")
                    else:
                        print("That number is not in the list.")
                except ValueError:
                    print("Please enter a number.")
        elif choice == "4":
            print("Going back to main menu...")
            break
        else:
            print("Please choose 1, 2, 3 or 4.")

# Tool 3: Expense Tracker - uses a list + loop + conditionals
def expense_tracker():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View expenses and total")
        print("3. Back to main menu")
        choice = input("Choose (1-3): ")

        if choice == "1":
            try:
                amount = float(input("Enter expense amount (Ksh): "))
                expenses.append(amount)
                print(f"Added Ksh {amount}")
            except ValueError:
                print("Please enter a number.")
        elif choice == "2":
            if len(expenses) == 0:
                print("No expenses yet.")
            else:
                print("Your expenses:")
                for i, amount in enumerate(expenses, start=1):
                    print(f"{i}. Ksh {amount}")
                print(f"Total spent: Ksh {sum(expenses)}")
                print(f"Number of expenses: {len(expenses)}")
        elif choice == "3":
            print("Going back to main menu...")
            break
        else:
            print("Please choose 1, 2 or 3.")

# MAIN PROGRAM - Menu loop runs until user quits
print("Welcome to your Personal Mini-Toolkit!")

while True:
    show_menu()
    main_choice = input("Choose a tool (1-4): ")

    if main_choice == "1":
        calculator()
    elif main_choice == "2":
        todo_manager()
    elif main_choice == "3":
        expense_tracker()
    elif main_choice == "4":
        print("Thank you for using your Mini-Toolkit. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")