"""
Module: script_06.py
Description: Demonstrates user defiend functions returning a function reference in python.
Documentation:
- We can return a function also from the return statement.
- We can also return a function that is defined outside of the function with return statement.
"""

def inner():
    print("Inner function called.")

def outer():
    return inner

inner_reference = outer()
inner_reference()
