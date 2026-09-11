"""
Module: script_06.py
Description: Demonstrates for loop with else and break statement in python.
Documentation:
- Python supports an else statement associated with a loop statement.
- In case of for loop, the else statement is executed when the condition becomes false.
- The for loop can be terminated with a break statement. In such case, the else part is ignored.
    Hence, a for loop's else part runs if no break occurs and the condition is false.

Use case:
- The main usecase for else statement is in search loops, where you are performing a search for an
    item and need to perform additional processing or throw an error, if search value is not found.

Break Statement:
- It brings control out of the loop.
- The purpose of this statement is to end the execution of the loop (for or while) immediately and
    the program control goes to the statement after the last statement of the loop.
"""

companies_list = ["TCS", "IBM", "INFY"]

for item in companies_list:
    if item == "HCL":
        print("HCL is in the list.")
        break
else:
    print("HCL is not in the list.")
