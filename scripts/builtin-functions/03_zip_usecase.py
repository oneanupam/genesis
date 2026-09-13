"""Map server names with their IP addresses"""

server_names = ["web-server-1", "web-server-2", "db-server-1", "db-server-2"]
server_ips = ["10.0.1.10", "10.0.1.11", "10.0.2.10", "10.0.2.11"]


def map_server_details(server_names: list[str], server_ips: list[str]) -> dict:
    """Function to map the server name with their IP addresses.

    Args:
        server_names (list[str]): list of server names
        server_ips (list[str]): list of IP addresses

    Returns:
        dict: dictionary of server details
    """
    # Zip to create an iterable
    server_details = zip(server_names, server_ips)
    # Convert iterable to a dictionary
    server_details_01 = dict(server_details)
    print(f"Server Details: {server_details}")
    return (server_details_01,)


def print_server_details(server_details: dict) -> dict | None:
    """Function to print the server details

    Args:
        server_details (dict): dictionary of server details
    """
    for key, value in server_details.items():
        print(f"Server Name: {key}, Server IP: {value}")


if __name__ == "__main__":
    result = map_server_details(server_names, server_ips)
    print_server_details(result)
