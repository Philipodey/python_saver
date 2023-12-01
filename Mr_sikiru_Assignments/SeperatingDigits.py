five_digit_number = int(input("Enter a five digit number: "))
# fiveValue = 0
# fourthValue = 0
# thirdValue = 0
# secondValue = 0
# last = 0
while 11111 > five_digit_number > 99999:
    print("Invalid number")
    five_digit_number = int(input("Enter a five digit number"))
count = 0
while 9999 < five_digit_number <= 99999:
    fiveValue = five_digit_number // 10000
    fourthValue = five_digit_number // 1000 % 10
    thirdValue = five_digit_number // 100 % 10
    secondValue = five_digit_number // 10 % 10
    last = five_digit_number % 10
    print(f"{fiveValue} {fourthValue} {thirdValue} {secondValue} {last}")
    break