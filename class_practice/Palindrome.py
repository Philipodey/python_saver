def is_palindrome(number):
    palindrome = bool(True)
    reverse_number = 0
    turn_number = number
    count = 0
    while number != 0:
        digit = number % 10
        reverse_number = reverse_number * 10 + digit
        number //= 10
    if reverse_number == turn_number:
        return palindrome
    else:
        return False


print(is_palindrome(1221))


