"""
Module: script_03.py
Description: Demonstrates user defiend functions in python.
Documentation:

Pass by value and Pass by reference:
- All the parameters in the python are passed by reference. That means, any change in the
    parameter inside a function reflects back the changes in the outside values as well.
"""

companies = ["TCS", "Infosys"]

def companies_list(org_list):
    """ A function to modify the list of companies."""

    org_list.append("HCL")
    print("Companies list inside the function: ", org_list)

# Calling the function with a list
companies_list(companies)
print(f"Companies list outside the function: {companies}")
