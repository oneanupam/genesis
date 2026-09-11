"""
Module: script_01.py
Description: Demonstrates user defiend functions in python.
Documentation:
- Defined by the "def" statement followed by the function name & parentheses ().
- Any args or input parameters should be placed within these parentheses.
- The functions first statement can be an optional statement, docstring.
    Docstring is the the documentation string of the function.
- To call a function, simply write the function's name followed by ()
    placing any required arguments within the brackets.
- You can check the docstring of a function by using __doc__ attribute of the function.

Returns:
- The function can return a value using the "return" statement.
- If no return statement is present, the function returns None by default.
- The optional return statement -> return (expression) exits a function,
    optionally passing back a value to the caller.
- Any statement written after the return statement will not be executed as return
    statement exits a function, passing back a value to the caller, if any else None.
- We can return a number, list, tuple, dictionary and Boolean values as well using return statement.
    We can also return multiple values using a single return statement. Python returns multiple values in a tuple.

Positional Arguments:
- Arguments must be passed to a function in the order they are defined.
- The number of arguments passed must match the number of parameters defined in the function.
- If fewer or more arguments are passed, it raises a TypeError.
- We can provide a default value to an argument by using the assignment operator (=).
    If you will not provide the value of that parameter then default value will be used.
"""

def add_function(value1: int = 10, value2: int = 10) -> tuple:
    """
    A function to add two integers.

    Args:
    value1 (int): The first integer to add.
    value2 (int): The second integer to add.

    Returns:
    int: The sum of value1 and value2.
    """
    operation = "Addition"
    result = value1 + value2
    return operation, result

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calling the function with positional arguments
output = add_function(num1, num2)
print(f"Type of output: {type(output)}")
print(f"{output[0]} Result: {output[1]}")
