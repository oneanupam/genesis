# ruff: noqa
# Simple function
def identity(x):
    return x


# Calling general function
print(identity(10))

# Lambda function and its call
return_value = (lambda x: x)(10)
print(return_value)
