# The Iterable (The container)
my_list = [10, 20, 30]

# Generating the Iterator (The bookmark)
my_iterator = iter(my_list)

# Manual stepping through the data stream
print(next(my_iterator))  # Output: 10
print(next(my_iterator))  # Output: 20
print(next(my_iterator))  # Output: 30

# This next line will raise a StopIteration exception
print(next(my_iterator))
