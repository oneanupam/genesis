services = ["GKE", "BigQuery", "Cloud SQL"]


def without_enumerate(services: list[str]) -> None:
    for index in range(len(services)):
        print(f"{index + 1} - {services[index]}")


def with_enumerate(services: list[str]) -> None:
    """Pythonic way of adding index to an iterable.

    Args:
        services (list[str]): list of google cloud services
    """
    for item in enumerate(services):
        print(f"{item}")
    for index, item in enumerate(services, start=1):
        print(f"{index} - {item}")


if __name__ == "__main__":
    without_enumerate(services)
    with_enumerate(services)
