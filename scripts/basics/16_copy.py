from copy import copy, deepcopy


# This is the demonstration of reference.
def just_reference():
    print("\n[INFO] just_reference function execution started...")

    gcp_services_category = ["Compute", "Database", "Network"]

    # Assignment operator only does the referencing.
    new_gcp_services_category = gcp_services_category
    print(f"Existing List: {gcp_services_category}")
    print(f"New List: {new_gcp_services_category}")

    if new_gcp_services_category is gcp_services_category:
        print(f"""Both the variable name points to same object in memory.
        ID of gcp_services_category: {id(gcp_services_category)}
        ID of new_gcp_services_category: {id(new_gcp_services_category)}
        """)
    else:
        print("A copy of the old object has been created")


# This is the demonstration of shallow copy
def the_shallow_copy():
    print("\n[INFO] the_shallow_copy function execution started...")

    gcp_services_category = ["Compute", "Database", "Network"]
    google_cloud_services = ["Compute", ["Cloud SQL", "Cloud Spanner"], "Network"]

    new_gcp_services_category = copy(gcp_services_category)
    if new_gcp_services_category is gcp_services_category:
        print("Both the variable name points to same object in memory")
    else:
        print("A copy of the old object has been created")

    new_google_cloud_services = copy(google_cloud_services)
    if new_google_cloud_services is google_cloud_services:
        print("Both the variable name points to same object in memory")
    else:
        print("A copy of the old object has been created")
    # shallow copy doesnt create the copy of nested objects, hence changing values in
    # nested object will change its value in parent list as well.
    new_google_cloud_services[1][0] = "Cloud Datastore"
    print(
        f"New List: {new_google_cloud_services} and Original List: {google_cloud_services}"
    )


# This is the demonstration of deep copy
def the_deep_copy():
    print("\n[INFO] the_deep_copy function execution started...")

    google_cloud_services = ["Compute", ["Cloud SQL", "Cloud Spanner"], "Network"]

    new_google_cloud_services = deepcopy(google_cloud_services)
    if new_google_cloud_services is google_cloud_services:
        print("Both the variable name points to same object in memory")
    else:
        print("A copy of the old object has been created")
    # shallow copy doesnt create the copy of nested objects, hence changing values in
    # nested object will change its value in parent list as well.
    new_google_cloud_services[1][0] = "Cloud Datastore"
    print(
        f"New List: {new_google_cloud_services} and Original List: {google_cloud_services}"
    )


just_reference()
the_shallow_copy()
the_deep_copy()
