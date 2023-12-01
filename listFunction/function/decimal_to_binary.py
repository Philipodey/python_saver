def decimal_to_binary(number: int):
    binary = 0
    value = ""

    while number != 0:
        digit = str(number % 2)
        value = value + digit
        number //= 2
    return value[-1::-1]


def binary_to_decimal(number):
    power = 0
    value = 0
    while number != 0:
        digit = number % 10
        value += digit * 2 ** power
        number //= 10
        power += 1
    return value
