dictionary = {2: 4, 1: 1, 3: 9, 5: 25, 4: 16}


# dictionary

def sort_dictionary(diction):
    sort_pair = {}
    for keys, values in diction.items():
        sort_pair = sorted(diction.items(), reverse=True)
    # return sort_pair
    return dict(sort_pair)


print(sort_dictionary(dictionary))


def add_to_dictionary(diction, item):
    diction.update(item)
    return diction


print(add_to_dictionary({0: 10, 1: 20}, {2: 30}))
