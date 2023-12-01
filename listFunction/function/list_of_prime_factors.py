def prime_number(number):
    prime_factor = [0 for count in range(number + 1)]
    prime_factor[1] = 1
    for count in range(2, number + 1):
        prime_factor[count] = count
    for count in range(4, number + 1, 2):
        prime_factor[count] = 4
    for count in range(3, int(number ** 0.5) + 1):
        if prime_factor[count] == 1:
            for counter in range(count * count, number + 1, count):
                if prime_factor[counter] == 1:
                    prime_factor[counter] = 1

    while number != 1:
        print(prime_factor[number], end=" ")
        number = number // prime_factor[number]
    return prime_factor[number]


print(prime_number(20))
