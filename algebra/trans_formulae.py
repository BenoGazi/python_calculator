from sympy import symbols, Eq, solve


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