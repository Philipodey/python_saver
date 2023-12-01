sample_list = [1, 3, 2, 5, 3, 4, 6, 4, 6, 9, 8, 2, 10, 8, 6, 12, 15, 10, 4, 6, 14]


def duplicates_remove(numbers: list):
    another_number = unique_even_elements_in_a_list(numbers)
    return set(another_number)


def unique_even_elements_in_a_list(numbers: list):
    another_list = [count for count in numbers if count % 2 == 0]
    return another_list


def unique_even_elements(numbers: list):
    new_list = []
    for count in numbers:
        if count % 2 == 0:
            new_list.append(count)

    another_list = remove_duplicate(new_list)

    return another_list


def remove_duplicate(numbers: list):
    new_list = []
    for count in numbers:
        if count not in new_list:
            new_list.append(count)
    return new_list


print(duplicates_remove(sample_list))
print(unique_even_elements(sample_list))
