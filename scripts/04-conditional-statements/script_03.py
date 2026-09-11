"""
Module: script_02.py
Description: Demonstrates conditional statements in python.
"""

user_list = ['bob', 'anupam', 'tony', "default"]
user = 'anupam'

if user in user_list:
    print(f"{user} exists in the user list.")
else:
    print(f"{user} does not exist in the user list.")
