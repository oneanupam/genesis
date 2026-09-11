"""
Module: script_03.py
Description: Demonstrates for loop in python.
Documentation:
- The for loop in Python is used to iterate over a sequence (list, tuple, string).
- Loop continues until we reach the last item in the sequence.

range():
- range function generates a sequence of numbers (whole numbers) in the form of a list,
    which is generally used to iterate over with for loops.
- range function can be used in three ways:
a)	range(stop)
b)	range(start, stop)
c)	range(start, stop, step)
Where,
	start -> specifies from where to start.
stop -> specifies the total nos to generate.
Step -> specifies the difference between each number in the sequence.

- Out of the three, 2 arguments are optional. i.e., Start and Step are the optional arguments.
- The sequence will start from 0 by default, if start is not specified.
- Default value of the step is 1, if not specified.
- The range(n) is of exclusive nature that is why it doesnt include the last number in the output.
    i.e., The given end point is never part of the generated result.
"""

companies_list = ["IBM", "TCS", "INFY", "WIPRO"]

for item in range(len(companies_list)):
    print(companies_list[item])
