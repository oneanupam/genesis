def decorator(func):

    def wrapper(employee_name):
        company_code = {"company_code": "100"}
        response = func(employee_name)
        response.update(company_code)
        return response

    return wrapper


def print_employee_details(name):
    employee_details = {"company": "HCL"}
    employee_details["name"] = name
    return employee_details


# This is manual decoration of a function
add_compnay_code = decorator(print_employee_details)

# calling the decorated function to get the result
print(add_compnay_code("anupam"))
