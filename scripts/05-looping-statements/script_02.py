"""
Module: script_02.py
Description: Demonstrates while loop with else statement in python.
Documentation:
- Python supports an else statement associated with a loop statement.
- In case of while loop, the else statement is executed when the condition becomes false.
- The while loop can be terminated with a break statement. In such case, the else part is ignored.
    Hence, a while loop's else part runs if no break occurs and the condition is false.

Use case:
- The main usecase for else statement is in search loops, where you are performing a search for an
    item and need to perform additional processing or throw an error, if search value is not found.
"""

companies_list = ["IBM", "TCS", "INFY", "WIPRO"]
search_value = "HCL"

inc = 0
while inc < len(companies_list):
    if companies_list[inc] == search_value:
        # Processing for item found
        print(f"{search_value} found in list.")
        break
    inc = inc + 1
else:
    # Processing for item not found
    print(f"{search_value} not found in list.")
