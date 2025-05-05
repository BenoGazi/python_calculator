from .linear_solver import solve_linear_equation, solve_simultaneous_equations
from .quad_solver import solve_quadratic, graph_quad
from .trans_formulae import change_of_subject
from menus.menu import algebra_menu
from .cubic_solver import cubic_grapher, cubic_solver

def algebra_handler():
    algebra_menu()
    sub_choice = input("Select 1, 2, 3, 4 or 5: ")
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
    elif sub_choice == "4":
        print("***QUADRATIC EQUATION*** ---- ax² + bx + c = 0")
        try:
            a = float(input("Enter value for a: "))
            b = float(input("Enter value for b: "))
            c = float(input("Enter value for c: "))
            
            # Solve quadratic
            result = solve_quadratic(a, b, c)

            # Check if there's an error
            if "error" in result:
                print(result["error"])
            else:
                # Function to format real or complex roots
                def format_root(r):
                    if r.imag == 0:
                        return f"{round(r.real, 2)}"
                    else:
                        sign = '+' if r.imag > 0 else '-'
                        return f"{round(r.real, 2)} {sign} {abs(round(r.imag, 2))}i"
                
                # Output roots
                print(f"Nature of roots: {result['nature']}")
                print(f"Discriminant: {result['discriminant']}")
                print(f"x = {format_root(result['root_1'])} | x = {format_root(result['root_2'])}")

                graph_quad(a, b, c)

        except ValueError:
            print("Please enter valid numbers.")

    elif sub_choice == "5":
        print("*** Cubic Function *** ----ax³ + bx² + cx + d = 0")
        try:
            a = float(input("Enter value for a: "))
            b = float(input("Enter value for b: "))
            c = float(input("Enter value for c: "))
            d = float(input("Enter value for d: "))
        except ValueError:
            print("Invalid Inputs")
            return
        result = cubic_solver(a, b, c, d)
        if "error" in result:
            print(result["error"])
            return
        print("\nReal Roots: ")
        for r in result["real_roots"]:
            print(f"x = {round(r, 2)}")
        if result["complex_roots"]:
            print("\nComplex Roots: ")
            for r in result["complex_roots"]:
                image = round(r.imag, 2)
                real = round(r.real, 2)
                sign = '+' if image >= 0 else '-'
                print(f"x = {real} {sign} {abs(image)}i")
        cubic_grapher(a, b, c, d)
    else:
            print("Invalid Option")