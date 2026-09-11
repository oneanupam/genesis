"""
Module: script_09.py
Description: Demonstrates functions using *args & **kwargs in python.
"""

def display_data(*args, **kwargs):
    """ Function to use the *args and **kwargs """

    print(type(args))
    for arg in args:
        print(arg)

    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, ":", value)

# Calling the function
display_data(68, 10, name="anupam", pin=96)
