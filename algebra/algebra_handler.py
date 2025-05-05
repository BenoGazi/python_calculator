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
            # Prompt user for coefficients a and b
            a = int(input("Enter value for a: "))
            b = int(input("Enter value for b: "))
            # Solve the linear equation and display result
            result = solve_linear_equation(a, b)
            print("solution", result)
        except ValueError:
            # Error handling for invalid input
            print("Please enter valid numbers")
    
    # Handle simultaneous equations solving
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

            # Solve the simultaneous equations and display result
            result = solve_simultaneous_equations(a1, b1, c1, a2, b2, c2)
            print("Solution: ", result)
        except ValueError:
            print("Invalid inputs. Please try again")
    
    # Handle change of subject in formulae
    elif sub_choice == "3":
        print("***Change of Subject***\n")
        formula = input("Enter the formula: For example(v = u + a * t): )")
        subject = input("Which variable do you want to make the subject?: ")
        # Perform the change of subject and display result
        result = change_of_subject(formula, subject)
        print(f"{subject} = {result[0]}")
    
    # Handle solving quadratic equations
    elif sub_choice == "4":
        print("***QUADRATIC EQUATION*** ---- ax² + bx + c = 0")
        try:
            # Input values for the quadratic equation coefficients
            a = float(input("Enter value for a: "))
            b = float(input("Enter value for b: "))
            c = float(input("Enter value for c: "))

            result = solve_quadratic(a, b, c)
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

                # Plot the quadratic graph
                graph_quad(a, b, c)

        except ValueError:
            # Error handling for invalid input
            print("Please enter valid numbers.")

    # Handle solving cubic equations
    elif sub_choice == "5":
        print("*** Cubic Function *** ----ax³ + bx² + cx + d = 0")
        try:
            a = float(input("Enter value for a: "))
            b = float(input("Enter value for b: "))
            c = float(input("Enter value for c: "))
            d = float(input("Enter value for d: "))
        except ValueError:
            # Error handling for invalid input
            print("Invalid Inputs")
            return
        
        # Solve the cubic equation and display result
        result = cubic_solver(a, b, c, d)
        
        # If there's an error, display it
        if "error" in result:
            print(result["error"])
            return
        
        # Display real roots
        print("\nReal Roots: ")
        for r in result["real_roots"]:
            print(f"x = {round(r, 2)}")
        
        # Display complex roots, if any
        if result["complex_roots"]:
            print("\nComplex Roots: ")
            for r in result["complex_roots"]:
                image = round(r.imag, 2)
                real = round(r.real, 2)
                sign = '+' if image >= 0 else '-'
                print(f"x = {real} {sign} {abs(image)}i")
        
        # Plot the cubic graph
        cubic_grapher(a, b, c, d)
    else:
        print("Invalid Option")
