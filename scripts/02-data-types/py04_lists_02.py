"""
Module: py04_lists_02.py
Description: Demonstrates built-in functions of lists in python.
"""

numbers = [33, 24, 1, 24, 9, 3]

# list functions
print(f"Length of the list: {len(numbers)}")
print(f"Minimum value in the list: {min(numbers)}")
print(f"Maximum value in the list: {max(numbers)}")

# Count: counts the occurrences of a value in the list
print(f"Occurrences of 24 in the list: {numbers.count(24)}")

# Append: Adds an element to the end of the list
numbers.append(100)
print(f"List after append an element: {numbers}")

# Extend: Adds elements from an iterable (like another list) to the end of the list
numbers.extend([200, 300])
print(f"List after extend with a list: {numbers}")

# Insert: Inserts an element at a specified index
numbers.insert(2, 50)  # Insert 50 at index 2
print(f"List after insert 50 at index 2: {numbers}")

# Remove/del: removes the element from the list
numbers.remove(24)  # Removes the first occurrence of 24
print(f"List after removing first occurrence of 24: {numbers}")

del numbers[0]  # Deletes the element at index 0
print(f"List after removing first element: {numbers}")

# Index: Returns the index of the first occurrence of a value in the list
index_of_9 = numbers.index(9)
print(f"Index of 9 in the list: {index_of_9}")

# Sort: Sorts the list in ascending order by default. Returns nothing but updates the list.
numbers.sort()  # This sorts the list in place
print(f"Sorted list: {numbers}")
