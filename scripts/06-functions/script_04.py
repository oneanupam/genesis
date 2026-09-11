"""
Module: script_04.py
Description: Demonstrates user defiend functions returning a function in python.
Documentation:
- We can return a function also from the return statement.
- We can also return a function that is defined outside of the function with return statement.
"""

def outer():
    def inner():
        print("Inner function called.")
    # returning function "inner" itself
    return inner()

outer()
