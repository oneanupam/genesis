"""
Module: script_08.py
Description: Demonstrates pass statement in python.
Documentation:
- In Python programming, pass is a null statement. Nothing happens when pass is executed.
    It results into no operation (NOP).

Use case:
- We generally use it as a placeholder.
- Suppose we have a loop or a function that is not implemented yet, but we want to implement it
    in the future. They cannot have an empty body. The interpreter would complain.
    So, we use the pass statement to construct a body that does nothing.
"""

num_list = [1, 2, 3, 4, 5]

for item in num_list:
    pass  # Placeholder for future implementation
