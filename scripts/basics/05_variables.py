"""
Module: py01_variables
Description: Demonstrates variables in python.
Documentation:
- To create a variable, you just assign it a value and then start using it. Assignment is done with
    a single equals sign (=). Python also allows chained assignment, which allows to assign the same
    value to several variables simultaneously.
- Python is dynamically typed. This means that you don't need to state the types of variables when
    you declare them
"""

a = "10"
b = c = d = 20

print(f"Variable a: {a}")
print(f"Type of variable a: {type(a)}")
print(f"Variable b: {b}, c: {c}, d: {d}")
print(f"Type of variable b: {type(b)}, c: {type(c)}, d: {type(d)}")
