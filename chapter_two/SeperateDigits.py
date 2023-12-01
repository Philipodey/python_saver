number = int(input('Enter the five digit number: '))
if 11111 > number > 99999:
    print("Invalid number")
    number = int(input("Enter five digit number: "))

first_digit = number // 10000
second_digit = number // 1000 % 10
third_digit = number // 100 % 10
fourth_digit = number // 10 % 10
fifth_digit = number // 1 % 10
print(f"{first_digit:>2}{second_digit:>2}{third_digit:>2}{fourth_digit:>2}{fifth_digit:>2}")

