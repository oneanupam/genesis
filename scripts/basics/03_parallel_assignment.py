# Pythonic Way
previous_value = 42
next_value = 43

next_value, previous_value = previous_value, next_value

print(previous_value)
print(next_value)

# Non-Pythonic Way
previous_value = 42
next_value = 43

temp = previous_value
previous_value = next_value
next_value = temp

print(previous_value)
print(next_value)
