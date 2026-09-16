def starts_a(word):
    return word.startswith("a")


fruites_list = ["apple", "banana", "avocado", "cherry", "apricot"]
result = filter(starts_a, fruites_list)

# convert the iterator to sequence
print(list(result))

# print(tuple(result))
# print(set(result))
# print({"".join(list(result))})
