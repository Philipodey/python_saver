def turn_tuple(numbers):
    reverse_tuple = ()
    for count in range(len(numbers)):
        reverse_tuple = reverse_tuple + (numbers[-count - 1],)
    return reverse_tuple


def remove_element(numbers):
    latest_tuple = ()
    for count in range(len(numbers)):
        number_second = (numbers[-2])
        number_three = (numbers[-1])
        new_second = (number_second[-2])
        new_third = (number_three[-1])

        latest_tuple = (new_second, (1, new_third))

        print(new_second)
        print(new_third)

        print(latest_tuple)
    return latest_tuple


def unpack_element(numbers):
    another_tuple = ()
    for count in range(len(numbers)):
        number_first = numbers[0]
        number_second = numbers[-1]
        another_tuple = number_second, number_first
    return another_tuple


# def appear_twice(numbers):
#     appear = ()
#     for count in numbers:
#         if count in appear:
#



    return None
