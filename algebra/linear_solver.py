import re
from sympy import Eq, solve, simplify, symbols
from sympy.parsing.sympy_parser import parse_expr


# def solve_linear_equation(a, b):
#     # Check if the equation is invalid (a cannot be 0 for a valid linear equation)
#     if a == 0:
#         if b == 0:
#             return "Infinite Solutions"  # If both a and b are 0, there are infinite solutions
#         else:
#             return "No Solution"  # If a is 0 but b is non-zero, no solution exists
    
#     # If a is not zero, solve for x using the linear equation x = -b/a
#     x = -b / a
#     return f"x = {x}"



def preprocess_equation(equation_str):
    #Inserts * between coefficients and variables (e.g., 6x -> 6*x)
    # Add * between digit and variable: '6x' -> '6*x'
    equation_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', equation_str)
    return equation_str

def solve_linear_equation_from_string(equation_str):

    #Solves a linear equation from a string like "3x+5x+2=4x+5x+9+8"
    try:
        # Remove spaces and preprocess for implicit multiplication
        equation_str = preprocess_equation(equation_str.replace(" ", ""))

        # Split into LHS and RHS
        lhs_str, rhs_str = equation_str.split("=")

        # Parse and simplify expressions
        lhs = simplify(parse_expr(lhs_str))
        rhs = simplify(parse_expr(rhs_str))

        # Form and solve the equation
        x = symbols('x')
        equation = Eq(lhs, rhs)
        solution = solve(equation, x)

        if not solution:
            return {"error": "No solution or infinite solutions."}

        return {"solution": solution[0], "equation": equation}

    except Exception as e:
        return {"error": f"Invalid input: {e}"}


def solve_simultaneous_equations(a1, b1, c1, a2, b2, c2):
    # Calculate the determinant to check if the system has a unique solution
    determinant = a1 * b2 - a2 * b1
    
    # If determinant is 0, the system has no solution (parallel lines)
    if determinant == 0:
        return "No Solution"
    
    # Calculate the values for x and y using Cramer's rule
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    
    # Return the values of x and y as a formatted string
    return f"x = {x}, y = {y}"
