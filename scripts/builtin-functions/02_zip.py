"""
Module: script_05.py
Description: Demonstrates parallel iteration using zip() in python.
Documentation:
- zip() function allows you to iterate in parallel over two or more iterables.
- Since zip() generates tuples, you can unpack these in the header of a for loop.
- If iterables are not of same length then zip() outputs will be equal to the length of the
    shortest iterable. The remaining elements in any longer iterables will be totally ignored
"""

# Demonstrating parallel iteration with list and tuple
companies_list = ["HCL", "TCS", "INFY", "WIPRO"]
total_employees = ("2L", "6L", "3L", "2L", "5L")

for compnay_name, total_employee in zip(companies_list, total_employees):
    print(f"Company: {compnay_name}, Total Employees: {total_employee}")

# Demonstrating parallel iteration with dictionaries
dict_one = {"name": "John", "last_name": "Doe", "job": "Python Consultant"}
dict_two = {"name": "Jane", "last_name": "Doe", "job": "Community Manager"}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, "->", v1)
    print(k2, "->", v2)
