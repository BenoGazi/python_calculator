def solve_linear_equation(a, b):
    # Check if the equation is invalid (a cannot be 0 for a valid linear equation)
    if a == 0:
        if b == 0:
            return "Infinite Solutions"  # If both a and b are 0, there are infinite solutions
        else:
            return "No Solution"  # If a is 0 but b is non-zero, no solution exists
    
    # If a is not zero, solve for x using the linear equation x = -b/a
    x = -b / a
    return f"x = {x}"

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
