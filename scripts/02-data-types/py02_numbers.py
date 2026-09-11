"""
Module: py02_numbers
Description: Demonstrates numbers in python.
Documentation:
- Python number data type is used to hold numeric values like: Integer, Float and Complex numbers
- Integers can be of any length; it is only limited by the memory available
- A floating point number is accurate up to 15 decimal places.
- Complex numbers are written in the form, x + yj, where x is real part & y is imaginary part
"""

import math
import random

a = 10
b = 20.50
c = 3 + 5j

print(f"Type of variable a: {type(a)}")
print(f"Type of variable b: {type(b)}, c: {type(c)}")

print(f"Min of two numbers: {min(a, b)}")
print(f"Max of two numbers: {max(a, b)}")

# Demonstrating some mathematical operations using math module
print(f"Ceil Value: {math.ceil(b)}")
print(f"Floor Value: {math.floor(b)}")

# Using random module to generate a random number
print(f"Random number between 1 and 100: {random.randint(1, 100)}")
