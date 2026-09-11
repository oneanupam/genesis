"""
Module: script_07.py
Description: Demonstrates user defiend functions with variable length parameters in python.
Documentation:
- Sometimes, we do not know in advance the number of arguments that will be passed into a function.
    Python allows us to handle this kind of situation through function calls with arbitrary number
    of arguments.

"*args" and "**kwargs":
- Both are used to take unlimited no of arguments and both prevents the program from crashing.
- "*args" takes unlimited no of arguments and "**kwargs" takes unlimited no of keyword arguments.
- In *args, unlimited no of arguments that we pass as a function argument are stored in a tuple
    So we generally we use loop inside the function to get the values of tuple. Whereas in **kwargs,
    unlimited no of keyword arguments that we pass as a function argument are stored in a dictionary
    Means, args is a tuple of positional arguments and kwargs is a dictionary of keyword arguments.
"""

# *args will take unlimited no of arguments and store them in a tuple
def users_data(*args):
    """ A function to display user data. """
    for item in args:
        print(item)

users_list = ["anupam", "tony"]
users_data(users_list)
