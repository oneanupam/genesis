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

# the logging module is a part of the Python standard library.
import logging

# Configure the log formatting
logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime}:{levelname}:{name}:{message}",
    style="{",
)

# Create a logger instance
logger = logging.getLogger(__name__)


# *args will take unlimited no of arguments and store them in a tuple
# The * here says: "Take whatever the user throws at me and pack it into a tuple called 'args'"
def users_data_01(*args):
    """A function to display user data."""
    logger.debug("executing the users_data_01 function")
    print(args)  # all the args are packed in a tuple
    for item in [*args]:
        print(item)


def users_data_02(name01, name02):
    """A function to display user data."""
    logger.debug("executing the users_data_02 function")
    # locals() returns a dictionary of all local variables currently defined in the function
    # [*...]: The * operator unpacks those values, and the outer brackets [] instantly pack them right back into a clean, standard Python list.
    names_list = [*locals().values()]
    for item in names_list:
        print(item)


def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result


list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

users_list = ["anupam", "tony"]

# The * here says: "Unzip this list and pour the items out individually"
users_data_01(*users_list)

# The * here says: "Unzip this list and pour the items out individually"
users_data_02(*users_list)

print(my_sum(*list1, *list2, *list3))


# merging the list using unpacking operator
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)

# unpack a string
a = [*"RealPython"]
print(a)
# Join it using join function
b = "".join(a)
print(b)

# With the trailing comma, you have defined a tuple with only one named variable
(*c,) = "RealPython"
print(c)
