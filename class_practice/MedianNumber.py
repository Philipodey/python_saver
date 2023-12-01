def median_number(number: list) -> list:
    for first in range(len(number)):
        for second in range(first + 1, len(number)):
            if number[first] > number[second]:
                number[first], number[second] = number[second], number[first]
    print(number)
    arrange_number = len(number)
    if arrange_number % 2 == 0:
        first_median = number[arrange_number // 2]
        second_median = number[(arrange_number // 2) - 1]
        median = (first_median + second_median) / 2
    else:
        median = number[arrange_number // 2]
    sum = 0
    for count in number:
        sum += count
    mean = sum / arrange_number
    print(sum)
    print(f"The median is {median}")
    print(f'The mean is {mean}')


median_number([10, 20, 15, 25, 5, 30, 35, 20, 10, 20])
