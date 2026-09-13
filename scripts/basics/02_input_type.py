"""
Module: script_03
Description: Demonstrates the use of input, print, and type functions to interact with user data.
Functions:
- input: Collects user input from the console.
- print: Outputs data to the console.
- type: Displays the data type of a variable.
"""

name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", user_age)

print("Type of name variable:", type(name))
print("Type of age variable:", type(user_age))

"""
Module: script_04
Description: Demonstrates the use of single line and multi-line statements in Python.
Example:
- Use line continuation character to denote that statement is in continuation.
- Use semicolon (;) to separate multiple statements on the same line.
- Statements contained within the ( ), { }, [ ] brackets dont need the use the line continuation character.
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)
