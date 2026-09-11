"""
Module: script_01.py
Description: Check if the key exists in the dictionary
"""

def check_key_existence(
        user_details: dict,
        key: str = "Pin"
        ) -> str:
    """
    Check if the key exists in the dictionary.

    Args:
        user_details (dict): dictionary containing user details
        key (str): key to check in the dictionary

    Returns:
        str: message indicating whether the key exists or not
    """
    if key in user_details:
        return f"{key} exists in the dictionary: {user_details[key]}"
    else:
        return f"{user_details.get(key, 'No Record Found')}"

if __name__ == "__main__":
    user_info = {'Name': 'Anupam', 'Pin': 96, 'Age': 30}
    key_to_check = 'Name'
    print(check_key_existence(user_info, key_to_check))
