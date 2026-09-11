"""
Module: script_02.py
Description: Demonstrates user defiend functions with named arguments in python.
Documentation:
Named Arguments:
- Unlike positional arguments, order doesnt matter for named arguments.
- In this case, you need to pass the parameter values with specified name defined in function.
"""

def display_data(name, age):
    """
    A function to display name and age.

    Args:
        name (str): The name of the person.
        age (int): The age of the person.

    Returns:
        None
    """
    print("Name: ", name)
    print("Age: ", age)

name_value = input("Enter your name: ")
age_value = int(input("Enter your age: "))

# Calling the function with named arguments
display_data(age = age_value, name = name_value)
