# ruff: noqa

# These two code blocks do the exact same thing:

# Shortcut 1: Generator Expression
big_generator = (x for x in range(10000000))


# Equivalent 2: Generator Function with Yield
def my_recipe():
    for x in range(10000000):
        yield x


big_generator = my_recipe()

# Parsing the values of a generator object
# Once you have created your generator object, you can then use next() to pull data out of it.
print(next(big_generator))
print(next(big_generator))
print(next(big_generator))
