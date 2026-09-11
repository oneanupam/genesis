"""
Module: script_04.py
Description: Demonstrates for loop using enumerate() in python.
Documentation:
- enumerate() function adds an index to each item in an iterable
    and returns it as an enumerate object, pairing each item with an index.
- enumerate() accepts an iterable and an optional start argument to set the initial index value.
- You can use zip() for iterating multiple sequences.
"""

companies_list = ["IBM", "TCS", "INFY", "WIPRO"]

for index, item in enumerate(companies_list):
    print(f"Index: {index}, Company: {item}")
