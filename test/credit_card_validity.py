def credit_card_number(card_number):
    result = ""
    if 13 <= int(len(card_number)) <= 16:
        if int(card_number[0]) == 4:
            result = "Visa card"
        elif int(card_number[0]) == 5:
            result = "MasterCard"
        elif int(card_number[0]) == 3 and card_number[1] == 7:
            result = "American Express Card"
        elif int(card_number[0]) == 6:
            result = "Discovery card"
        else:
            result = "invalid card"
    else:
        result = "Invalid length"
    return result


def credit_card_validate(card_number):
    odd_multiply = 1
    even_add = 0
    odd_add_total = 0
    odd_add_one = 0
    odd_add_two = 0
    digit_add = 0
    for count in card_number[len(card_number) - 2:: -2]:
        odd_multiply = int(count) * 2
        if odd_multiply > 9:
            digit_one = odd_multiply % 10
            digit_two = odd_multiply // 10
            digit_add = digit_two + digit_one
            odd_add_one += digit_add
        else:
            odd_add_two += odd_multiply
    odd_add_total = odd_add_one + odd_add_two
    for counter in card_number[len(card_number) - 1: 0: -2]:
        even_add += int(counter)
    validateAdd = odd_add_total + even_add
    if validateAdd % 10 == 0:
        return "Valid"
    else:
        return "Invalid"
