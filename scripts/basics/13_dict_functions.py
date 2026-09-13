"""
Module: py05_dicts_02.py
Description: Demonstrates dictionaries in python.
"""

dict_01 = {"Name": "Anupam", "Pin": 96}

# Dictionary functions
print(f"Length of the dictionary: {len(dict_01)}")
print(f"Keys in the dictionary: {dict_01.keys()}")
print(f"Values in the dictionary: {dict_01.values()}")

# Items: Returns a view object that displays a list of a dictionary's key-value tuple pairs
print(f"Items in the dictionary: {dict_01.items()}")
for key, value in dict_01.items():
    print(key, value)

for item in dict_01.values():
    print(item)

# Get: Returns the value for a specified key if it exists, otherwise returns None or a default value
dict_01 = {"Name": "Anupam", "Pin": 96}
print(f"Get value for 'Address': {dict_01.get('Address', 'Unknown')}")

# Update: Updates the dictionary with the specified key-value pairs
dict_01.update({"Age": 30, "City": "New York"})
print(f"Dictionary after update: {dict_01}")
