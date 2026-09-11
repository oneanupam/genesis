"""
Module: py05_tuples_01.py
Description: Demonstrates lists in python.
Documentation:
- Tuple is an ordered sequence of items same as list. The only difference is that
    tuples are immutable. Tuples once created cannot be modified.
- Values are separated by commas and enclosed within parenthesis ( ).
- Processing of tuples are faster than list because in tuples, data is open in read only mode.
"""

# Creating a tuple using tuple() function
# If no argument is given, the constructor creates a new empty tuple.
# The argument must be an iterable if specified.
tuple_01 = tuple()
print(f"Type of object: {type(tuple_01)}")

# Creating a tuple using parenthesis
# Recommended as it is faster as it avoids an additional function call.
tuple_02 = ()
print(f"Type of object: {type(tuple_02)}")

# Creating a tuple with values
tuple_03 = (1)
print(f"Type of object: {type(tuple_03)}")

# Creating a tuple with a single value requires a trailing comma
tuple_04 = (1,)
print(f"Type of object: {type(tuple_04)}")

# An individual element from a tuple can not be deleted, but entire tuple can be using del keyword.
tuple_05 = (1, 2, 3, 4, 5)
# del tuple_05[0]  # This will raise a TypeError
del tuple_05  # This will delete the entire tuple
print(f"Tuple 05: {tuple_05}")
