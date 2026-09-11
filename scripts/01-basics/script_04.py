"""
Module: script_04
Description: Demonstrates the use of single line and multi-line statements in Python.
Example:
- Use line continuation character to denote that statement is in continuation.
- Use semicolon (;) to separate multiple statements on the same line.
- Statements contained within the ( ), { }, [ ] brackets dont need the use the line continuation character.
"""

name = input("Enter your name: "); age = int(input("Enter your age: "));

print("Name:", \
      name)
print("Age:", age)
