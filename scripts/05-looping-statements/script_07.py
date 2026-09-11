"""
Module: script_07.py
Description: Demonstrates for loop with else and continue statement in python.
Documentation:
- The continue statement is used to skip the rest of the code inside a loop for the current
    iteration only. Loop does not terminate but continues on with the next iteration.
"""

num_list = [1, 2, 3, 4, 5]

for item in num_list:
    if item % 2 == 0: # Check if the remainder is 0 when divided by 2
        continue
    print(item)
