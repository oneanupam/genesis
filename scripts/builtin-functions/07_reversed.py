actions = ["Type text", "Select text", "Cut text", "Paste text"]

# exhausting this returned iterator using loop
for action in reversed(actions):
    print(action)

students = {
    "Alice": 89.5,
    "Bob": 76.0,
    "Charlie": 92.3,
    "Diana": 84.7,
    "Ethan": 88.9,
    "Fiona": 95.6,
    "George": 73.4,
    "Hannah": 81.2,
}

print(reversed(students.keys()))
