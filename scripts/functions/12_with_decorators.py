import time


# decorator function to add the additional data
def timer(func):

    def wrapper(employee_name):
        start_time = time.perf_counter()
        company_code = {"company_code": "100"}
        response = func(employee_name)
        response.update(company_code)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Time taken by {func.__name__}: {run_time}")

        return response

    return wrapper


@timer
def print_employee_details(name):
    employee_details = {"company": "HCL"}
    employee_details["name"] = name
    return employee_details


print(print_employee_details("anupam"))
