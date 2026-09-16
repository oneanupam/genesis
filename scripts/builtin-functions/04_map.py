# ruff: noqa
def double(value):
    return value * 2


numbers = [1, 2, 3, 4]
result = map(double, numbers)
print(list(result))

# Use of lambda function
result_02 = map(lambda num: num * 2, numbers)
print(list(result_02))
