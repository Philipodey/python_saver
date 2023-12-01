def divide_or_square(number: int) -> float:
    for count in range(number):
        count = 1
        if number % 5 == 0:
            return number * number
        else:
            return number ** 0.50


print(divide_or_square(76))
