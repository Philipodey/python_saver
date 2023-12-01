from typing import List


def largest(number):
    maximum = 0
    for count in number:
        if count > maximum:
            maximum = count
        return maximum


def reverse_element(number):
    reverse_number = []
    for count in number[::-1]:
        reverse_number.append(count)
    return reverse_number


def element_exit(number, integer):
    for count in number:
        if count == integer:
            return True


def element_on_odd_position(number):
    numbers = []
    for count in number[1::2]:
        numbers.append(count)
    return numbers


def element_on_even_position(number):
    numbers = []
    for count in number[::2]:
        numbers.append(count)
    return numbers


def commute_total_of_all_element(number):
    total = 0
    for count in number:
        total += count
    return total


def string_is_palindrome(characters):
    return characters == characters[::-1]


def concatenate_two_lists(first_list, second_list):
    merge_list = []
    for i in first_list:
        merge_list.append(i)
    for j in second_list:
        merge_list.append(j)
    return merge_list


def combines_two_list(first_list, second_list):
    merge_list = []
    count = 0
    for i in first_list:
        merge_list.append(i)
        merge_list.append(second_list[count])
        count += 1
    return merge_list


char = ['a', 'b', 'c']
integer = [1, 2, 3]
print(concatenate_two_lists(char, integer))

# lists = "wat"
# print(string_is_palindrome(lists))
