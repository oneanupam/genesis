costcenter = 45456  # A global variable


def update_costcenter():
    global costcenter  # Declares 'counter' as a global variable
    costcenter = costcenter + 1
    return costcenter


print(update_costcenter())
