"""
Module: script_05.py
Description: Demonstrates user defiend functions returning a function reference in python.
Documentation:
- We can return a function also from the return statement.
- We can also return a function that is defined outside of the function with return statement.
"""

def outer():
    def inner():
        print("Inner function called.")
    # returning a reference to the function "inner"
    return inner

inner_reference = outer()
inner_reference()
