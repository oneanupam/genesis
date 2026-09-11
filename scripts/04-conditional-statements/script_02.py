"""
Module: script_03.py
Description: Demonstrates conditional operator or ternary operator in python.
Documentation:
- Python supports one additional decision-making entity called a conditional expression. (It is also
    referred to as a conditional operator or ternary operator in various places in the Python
    documentation.)
 - In the below example, <conditional_expression> is evaluated first. If it is true, the expression
    evaluates to <expression1>. If it is false, the expression evaluates to <expression2>.
Syntax:
<expression1> if <conditional_expression> else <expression2>
"""

user_info = {'name': 'anupam', 'pin': 96, 'age': 30}
key = 'name'

print(f"{key} exists in the dictionary: {user_info.get(key)}") if(key in user_info) else print("Key not found")
