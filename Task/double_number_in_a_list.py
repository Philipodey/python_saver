def double_number_in_list(numbers: str):
    string = numbers.split(",")
    new_list = []
    count = 0
    for index in string:
        num = int(index) * int(index)
        new_list.append(num)
    return new_list


number = "2, 3, 4"

print(double_number_in_list(number))
