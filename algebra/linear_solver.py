
def solve_linear_equation(a, b):
    if a == 0:
        if b == 0:
            return "Infinite Solutions"
        else:
            return "No Solution"
    x = -b / a
    return f"x = {x}"

def solve_simultaneous_equations(a1, b1, c1, a2, b2, c2):
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return "No Solution"
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    return f"x = {x}, y = {y}"