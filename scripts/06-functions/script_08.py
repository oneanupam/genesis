"""
Module: script_08.py
Description: Demonstrates user defiend functions with variable length parameters in python.
Documentation:
- **kwargs will take unlimited no of keyword arguments and store them in a dictionary
"""

# **kwargs will take unlimited no of keyword arguments and store them in a dictionary
def user_data(**kwargs):
    """ A function to display user data with keyword arguments. """
    print(kwargs)
    for key, value in kwargs.items():
        print(key, ":", value)

user_data(name="anupam", age=24)
