"""
Module: script_10.py
Description: Demonstrates functions using positional, named and variable length params in python.
Documentation:
- When working with positional parameters along with named keyword parameters in addition to
    "*args" and "**kwargs", your function would look like this:
        arg_1, arg_2, *args, kw_1="abc", kw_2="xyz", **kwargs

- It is important to keep the order of arguments in mind when creating functions so that you
    do not receive a syntax error in your Python code.
"""

def display_data(num, *args, city="delhi", **kwargs):
    """ Function to use the *args and **kwargs """

    # Positional argument
    print(f"positional argument value: {num}")

    # Varibale length arguments
    print(type(args))
    for arg in args:
        print(arg)

    # Named arguments
    print(f"Named argument value: {city}")

    # Variable length keyworded arguments
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, ":", value)

# Calling the function
display_data(24, 68, 10, city="noida", name="anupam", pin=96)
