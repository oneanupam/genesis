"""
Module: script_01.py
Description: Demonstrates while loop in python.
Documentation:
- Loops are used in programming to repeat a specific block of code until the given
    expression/condition is true.
- There are only two types of loop in Python. 1) for 2) while
- In while loop, Expression/Given condition is checked first. The body of the loop
    is entered only if the expression evaluates to True.
"""

# Program to demonstrate while lopp using table of 2
iterator = 1
number = 2

while iterator <= 10:
    value = number * iterator
    print(value)
    iterator = iterator + 1
