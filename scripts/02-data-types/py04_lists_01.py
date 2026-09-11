"""
Module: py04_lists_01.py
Description: Demonstrates lists in python.
Documentation:
- List is a hybrid data type.
- List is an ordered data type.
- List is a mutable data type. Means, its values can be updated.
- Values are separated by commas and enclosed within square brackets [ ].
"""

import copy

# Creating a list using list() function
# If no argument is given, the constructor creates a new empty list.
# The argument must be an iterable if specified.
# iterable: An object capable of returning its members one at a time (string, tuple, set, dict, etc.)
list_01 = list()

# Creating a list using square brackets
# Recommended as it is faster as it avoids an additional function call.
list_02 = []

companies = ["hcl", "tcs", "google", "microsoft", "amazon"]
# Accessing elements in a list using index
print(f"First company: {companies[0]}")
print(f"Last company: {companies[-1]}")

# Reference and Copy operations for lists
# Reference: Both variables point to the same list object in memory.
# Copy: Creates a new list object in memory with the same values.

list_03 = [1, 2, 3, 4, 5]
list_04 = list_03  # Reference

print(f"List 03: {list_03}")
print(f"List 04: {list_04}")

# Reference implementation
# Modifying list_04 will also modify list_03 since they reference the same object
list_04[0] = 10
print(f"List 03: {list_03}")
print(f"List 04: {list_04}")

# Shallow copy implementation
# Shallow copy creates a new list object but does not create copies of nested objects.
list_05 = copy.copy(list_03)
print(f"List 05: {list_05}")
# Modifying list_05 will not affect list_03
list_05[0] = 20
print("Demonstrating shallow copy:")
print(f"List 03: {list_03}")
print(f"List 05: {list_05}")

# Deep copy implementation
list_11 = [1, 2, [31, 32, [33, 34]], 4, 5]
list_12 = copy.deepcopy(list_11)  # Deep Copy
list_12[2][2][0] = 100
print("Demonstrating deep copy:")
print(f"List 11: {list_11}")
print(f"List 12: {list_12}")
