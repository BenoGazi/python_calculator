from sympy import symbols, Eq, solve

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


def change_of_subject(equation_str, subject_str):
    try:
      #Split equation into left and right sides
      lhs_str, rhs_str = equation_str.replace(" ", "").split("=")

      #Extract all variables
      vars = set(filter(str.isalpha, lhs_str + rhs_str))
      sympy_vars = symbols(" ".join(vars))

      #map variable names to sympy symbols
      var_map = {str(i): i for i in sympy_vars}

      #Evaluate  both sides using the variable map
      lhs = eval(lhs_str, {}, var_map)
      rhs = eval(rhs_str, {}, var_map)

      #Build symbolic equation
      equation = Eq(lhs, rhs)

      #Solve for the transposition
      result = solve(equation, var_map[subject_str])
      
      return result

    except Exception as e:
        return f"Error: {e}"
