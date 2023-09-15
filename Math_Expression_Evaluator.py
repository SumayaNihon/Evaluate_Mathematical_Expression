def evaluate_expression(expression):
    valid_characters = '0123456789+-*/(). '
    if not all(char in valid_characters for char in expression):
        return "Error: Invalid characters in the expression."

    code = f"result = {expression}"

    try:
        exec(code, globals(), locals())
        return locals().get('result')
    except ZeroDivisionError:
        return "Error: Division by zero."
    except Exception as e:
        return f"Error: {str(e)}"


result = evaluate_expression(input("Enter a mathematical expression: "))
print(f"Evaluated Result: {result}")
