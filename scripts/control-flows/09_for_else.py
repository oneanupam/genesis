numbers = [1, 3, 5, 7, 9]
target = 7


def without_else(seq, target):
    """Find the index of the first occurrence of `target` in `seq`."""

    found = False  # a flag variable
    for index, number in enumerate(seq):
        if number == target:
            print(f"Target found {target}!")
            found = True
            break

    if not found:
        return -1

    return index


def with_else(seq, target):
    for index, number in enumerate(seq):
        if number == target:
            print(f"Target found {target}!")
            break
    else:
        print(f"Target not found {target}")
        return -1

    return index


print(without_else(numbers, target))
print(with_else(numbers, target))
