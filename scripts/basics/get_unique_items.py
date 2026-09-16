# ruff: noqa
def get_unique_items(list_object):
    result = []
    for item in list_object:
        if item not in result:
            result.append(item)
    return result


print(get_unique_items([2, 4, 5, 2, 3, 5]))

# shortcut
print(list(set([2, 4, 5, 2, 3, 5])))
