import re

def arithmetic_expr(expr):
    # Check if the expression contains only valid characters (digits, operators, and decimal points)
    if not re.fullmatch(r'[\d\s\.\+\-\*/\(\)]+', expr):
        return {"error": "Invalid Numbers"}  # Return error if invalid characters are detected
    
    try:
        # Evaluate the arithmetic expression using the eval function
        result = eval(expr)
        return {"result": result}  # Return the result if the expression is valid

    except ZeroDivisionError:
        # Handle division by zero error and return an appropriate message
        return {"error": "Division by zero"}

    except Exception:
        # Catch any other exceptions (invalid expressions) and return an error message
        return {"error": "invalid expression"}
