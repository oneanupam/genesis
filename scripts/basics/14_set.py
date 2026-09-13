"""
Module: py07_set_01.py
Description: Demonstrates set data type in python.
Documentation:
Python set is a mutable and unordered collection of unique and hashable elements.
A set can store any type of element that is immutable.

- Mutable: You can add or remove elements from an existing set.
- Unordered: A set doesnt maintain any particular order of its elements.
- Unique elements: Duplicate elements are not allowed.
- Hashable elements: Each element must have a hash value that stays the same for its lifetime.

Difference b/w List and Set
- List is ordered and indexable, but set is not ordered and indexable
- List allows duplicates, but set doesnt.
    If you create a set with duplicate elements, the resulting set wont have any duplicate elements.
- List can store any type of object, but set can only store immutable objects
- List and set both are immutable.
- Lookup operation in set using membership operator ("in" and "not in") is faster than list.

Use-case:
- Use list, if you need ordered collection of items with duplicates
- Use set, if you need fast lookup, remove duplicates, set operations (union, intersection)
"""

# Creating a set using the set() constructor function
set_01 = set()
print(f"Type of the object: {type(set_01)}")

# Create set using literals
set_02 = {"anupam"}
set_03 = {96, "anupam"}
set_04 = {42, "Hi!", 3.14159, None, "Python"}

print(set_02, set_03, set_04)
