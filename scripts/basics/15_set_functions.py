"""
Module: py07_set_02.py
Description: Demonstrates built-in functions of set data type in python.
"""

# Creating a set using literal
set_01 = {"anupam", 96}

# Add and remove a single element from an existing set
set_01.add(False)
print(f"Set data after adding a value: {set_01}")

set_01.remove(96)
print(f"Set data after removing an element: {set_01}")

# .remove(), the .discard() method allows you to remove a single element from an existing set.
# Diff b/w both methods is that .discard() doesn’t raise an exception if the element doesn’t exist:
# set_01.remove("hcl")
set_01.discard("hcl")
print(f"Set data after removing an element: {set_01}")

# Removing and Returning an Element With .pop()
set_02 = {"anupam", "google", "hcl"}
print(f"Set data after removing an element using pop: {set_02.pop()}")
