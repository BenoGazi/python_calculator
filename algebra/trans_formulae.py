from sympy import symbols, Eq, solve

def change_of_subject(equation_str, subject_str):
    try:
        # Split the equation into left-hand side (lhs) and right-hand side (rhs)
        lhs_str, rhs_str = equation_str.replace(" ", "").split("=")

        # Extract all variables by filtering out alphabetic characters from lhs and rhs
        vars = set(filter(str.isalpha, lhs_str + rhs_str))
        
        # Create sympy symbols for the variables in the equation
        sympy_vars = symbols(" ".join(vars))

        # Map the variable names to corresponding sympy symbols
        var_map = {str(i): i for i in sympy_vars}

        # Evaluate both sides (lhs and rhs) of the equation using the variable map
        lhs = eval(lhs_str, {}, var_map)
        rhs = eval(rhs_str, {}, var_map)

        # Build a symbolic equation using the sympy Eq() function
        equation = Eq(lhs, rhs)

        # Solve for the variable to be made the subject (subject_str)
        result = solve(equation, var_map[subject_str])
        
        # Return the result (the expression with the subject isolated)
        return result

    except Exception as e:
        # Catch and return any errors that occur
        return f"Error: {e}"
