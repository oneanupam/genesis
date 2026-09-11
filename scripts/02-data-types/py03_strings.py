"""
Module: py03_strings
Description: Demonstrates strings in python.
Documentation:
- String is sequence of Unicode characters.
- We can use single quotes or double quotes to represent strings.
- A string in Python can contain as many characters as you wish. The only limit is your
    machines memory resources.
- In Python, Multi-line strings can be denoted using triple quotes (either single or double).
"""

company = "hcl technologies"
file_name = "hcl_5178xxxx.jpeg"
user_name = "Anupam Yadav"
address = "**New Delhi**"

print(f"Type of variable company: {type(company)}")
print(f"Length of string: {len(company)}")

# This function capitalizes the first letter of a string
print(f"First character: {company.capitalize()}")

#  This function converts first letter of all the word in to uppercase letter in a string
print(f"First character of each word: {company.title()}")

# Starts with and ends with functions
print(f"Filename starts with: {file_name.startswith('hcl')}")
print(f"Filename ends with: {file_name.endswith('.jpeg')}")

# find and replace functions for string
# find function:
# find checks that a given string occurs in the string or substring of the string.
# Returns starting index position of the string, if found otherwise returns -1.
print(f"Index of 'technologies': {company.find('technologies')}")
print(f"New Name: {company.replace(' technologies', 'tech')}")

# split and join function for strings
full_name = user_name.split(" ")
print(f"Splitted values: {full_name}")

# join function to concatenate strings
separator = "_"
print(f"Joined values: {separator.join(full_name)}")

# lstrip, rstrip and strip functions for strings
print(f"Left stripped address: {address.lstrip('*')}")
print(f"Right stripped address: {address.rstrip('*')}")
print(f"Stripped address: {address.strip('*')}")
