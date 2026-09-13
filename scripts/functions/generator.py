# Use generators by default for 90% of your data-streaming needs. They are cleaner, faster to write, and
# easier to maintain.


# 1. Iterator created using Generator function
def sequence_generator(sequence):
    for item in sequence:
        yield item


# 1. Parsing the values of a generator object using for loop
# All generators are iterators.
print("[INFO]: Calling generator object using for() loop...")
for item in sequence_generator([1, 2, 3, 4, 5]):
    print(item)

# 1. Initialize the generator with custom parameters
# This sets up the recipe: "Count from 10 to 50, going up by 15"
my_gen = sequence_generator([1, 2, 3])

# 2. The generator sits paused until you call next()
print("[INFO]: Calling generator object using next() function...")
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
