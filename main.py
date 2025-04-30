from menu import show_main_menu, arithmetic_menu
from basic_arithmetic import add, subtract, multiply, divide
from algebra import solve_linear_equation, solve_simultaneous_equations, change_of_subject


def arithmetic_handler():
    while True:
        arithmetic_menu()
        choice = input("Select your operation: 1-5: ")
        if choice == "5":
            print("Bye!")
            break
        if choice in ["1", "2", "3", "4"]:
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
        else:
            print("Invalid Option, Try Again.")

def algebra_handler():
    print("***ALGEBRA***\n")
    print("1. Linear Equation (ax +b = 0)")
    print("2. Simultaneous Equations")
    print("3. Transposition of Formulae")
    sub_choice = input("Select 1, 2 or 3: ")
    if sub_choice == "1":
        try:
            a = int(input("Enter value for a: "))
            b = int(input("Enter value for b: "))
            result = solve_linear_equation(a, b)
            print("solution", result)
        except ValueError:
            print("Please enter valid numbers")
    elif sub_choice == "2":
        try:
            print("Enter values for equation 1: a1, b1, c1")
            a1 = int(input("Value for a1: "))
            b1 = int(input("Value for b1: "))
            c1 = int(input("Value for c1: "))

            print("Enter Values for equation 2: ")
            a2 = int(input("Value for a2: "))
            b2 = int(input("Value for b2: "))
            c2 = int(input("Value for c2: "))

            result = solve_simultaneous_equations(a1, b1, c1, a2, b2, c2)
            print("Solution: ", result)
        except ValueError:
            print("Invalid inputs. Please try again")
    elif sub_choice == "3":
        print("***Change of Subject***\n")
        formula = input("Enter the formula: For example(v = u + a * t): )")
        subject = input("Which varibale do you want to make the subject?: ")
        result = change_of_subject(formula, subject)
        print(f"{subject} = {result[0]}")
    else:
        print("Invalid Option")



def main():
    while True:
        show_main_menu()
        choice = input("Enter your option number: ")
        if choice == "1":
            arithmetic_handler()
        elif choice == "2":
            algebra_handler()
        elif choice == "3":
            # simultaneous_handler()
            print("Simultaneous Calculator Under Construction")
        elif choice == "4":
            #transposition_handler()
            print("Transposition Calculator Under Construction...")
        else:
            print("Invalid choice, try again")
if __name__ == "__main__":
    main()
            
