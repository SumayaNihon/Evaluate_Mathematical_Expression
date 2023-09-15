# Evaluate_Mathematical_Expression
# Mathematical Expression Evaluator

This Python utility allows you to evaluate mathematical expressions provided as strings. It uses the `exec()` function to dynamically execute Python code and calculate the result of the expression.

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Supported Operators](#supported-operators)
- [Error Handling](#error-handling)
- [Output](#output)
- [Code](#code)


## Overview

The `evaluate_expression` function is designed to evaluate basic mathematical expressions that consist of numbers, operators (addition, subtraction, multiplication, division), and parentheses.

## Usage

To use the `evaluate_expression` function, follow these steps:

1. Import the function into your Python script or environment.
2. Call the function with a mathematical expression as a string.
3. The function will return the result of the evaluated expression.

## Supported Operators

The function supports the following mathematical operators:

- (+) (Addition)
- (-) (Subtraction)
- (*) (Multiplication)
- (/) (Division)

## Error Handling
The evaluate_expression function includes error handling to provide informative error messages:

* If the input expression contains invalid characters, it returns an error message indicating invalid characters in the expression.
* If a division by zero error occurs, it returns an error message indicating division by zero.
* For all other exceptions, it returns a generic error message.

## Output

`Enter a mathematical expression: (10-2)*2+(6/2)`
`Evaluated Result: 19.0`


## Code

   ```python
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
