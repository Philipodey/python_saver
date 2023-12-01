list_number = [[2, 4, 5, 6], [2, 3, 5, 6]]


def sum_list(numbers: list):
    total = 0
    for i in numbers:
        for j in i:
            total += j
    return total


print(sum_list(list_number))


def sum_list2(numbers2: list):
    numbers, numbers0 = numbers2
    total = numbers + numbers0
    total = sum(total)
    return total


print(sum_list2(list_number))
