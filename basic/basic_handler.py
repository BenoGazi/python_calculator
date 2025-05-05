from menus.menu import arithmetic_menu
from basic.basic_arithmetic import add, subtract, multiply, divide
from basic.expr_eval import arithmetic_expr
def arithmetic_handler():
    while True:
        arithmetic_menu()
        choice = input("Select your operation: 1-6: ")
        if choice  == "5":
            expression = input("Enter your Expression: ")
            result = arithmetic_expr(expression)
            if "error" in result:
                print("Error: ", result["error"])
            else:
                print(f"Result: = {result['result']}")
        elif choice == "6":
            break
        elif choice in ["1", "2", "3", "4", "6"]:
            try:
                num_1 = int(input("Enter the first number"))
                num_2 = int(input("Enter the second number: "))
            except ValueError:
                print("Please enter valid numbers.")
                continue
        if choice == "1":
            print(f"{num_1} + {num_2} = {add(num_1, num_2)}")
        elif choice == "2":
            print(f"{num_1} - {num_2}  = {subtract(num_1, num_2)}")
        elif choice == "3":
            print(f"{num_1} * {num_2} = {multiply(num_1, num_2)}")
        elif choice == "4":
            print(f"{num_1} / {num_2} = {divide(num_1,  num_2)}")
            pass
        else:
            print("Invalid Option, Try Again.")