"""
Module: script_01.py
Description: Demonstrates conditional statements in python.
"""

user_info = {'name': 'anupam', 'pin': 96, 'age': 30}
key = 'name'

if key in user_info:
    # print(f"{key} exists in the dictionary: {user_info[key]}")
    print(f"{key} exists in the dictionary: {user_info.get(key)}")
else:
    print(f"{key} does not exist in the dictionary")
