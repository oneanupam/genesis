import functools


# decorator function to add the additional data
def add_compnay_code(func):

    @functools.wraps(func)
    def wrapper(employee_name):
        company_code = {"company_code": "100"}
        response = func(employee_name)
        response.update(company_code)
        return response

    return wrapper


@add_compnay_code
def print_employee_details(name):
    employee_details = {"company": "HCL"}
    employee_details["name"] = name
    # check function identity, its name is now changed.
    print(print_employee_details.__name__)
    return employee_details


print(print_employee_details("anupam"))
