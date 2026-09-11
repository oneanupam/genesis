"""
Module: script_02.py
Description: Demonstrates switch equivalent in python.
Documentation:
- Python does not have a built-in switch statement like some other languages, but you can achieve
    similar functionality using dictionaries or if-elif-else statements.
- The example below uses a dictionary to simulate a switch statement.
- Python uses dictionary mapping to implement switch statement in Python.
"""

switcher = {
    1 : "Tata Consultancy Services",
    2 : "Infosys",
    3 : "HCL Technologies",
}

rank = int(input("Enter the ranking: "))
print(switcher.get(rank, "No Record Found."))
