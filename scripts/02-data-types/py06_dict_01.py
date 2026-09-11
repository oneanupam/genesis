"""
Module: py05_dicts_01.py
Description: Demonstrates dictionaries in python.
Documentation:
- Python Dictionary is an unordered sequence of data of key-value pair form.
- In Python 3.6 and beyond, dictionaries are ordered collections, meaning they keep their
    elements in the same order in which they were introduced.
- Dictionaries are written within curly braces { } in the form key : value.
- Keys must be immutable (ex: strings, numbers, tuples). Values can be any object.
- Keys must be unique, otherwise second one will win.
"""

# Creating a dictionary using dict() function
# If no argument is given, the constructor creates a new empty dictionary.
dict_01 = dict()
print(f"Type of object: {type(dict_01)}")

# Creating a dictionary using curly braces
# Recommended as it is faster as it avoids an additional function call.
dict_02 = {}
print(f"Type of object: {type(dict_02)}")


dict_03 = {'Name': 'Anupam', 'Pin': 96}

# Accessing elements in a dictionary using keys
print(f"Name: {dict_03['Name']}")
print(f"Pin: {dict_03['Pin']}")

# Adding a new key-value pair
dict_03['Age'] = 30
print(f"Dictionary after adding Age: {dict_03}")

# Updating an existing key-value pair
dict_03['Age'] = 31
print(f"Dictionary after updating Age: {dict_03}")

# Deleting a key-value pair
del dict_03['Pin']
print(f"Dictionary after deleting Pin: {dict_03}")
