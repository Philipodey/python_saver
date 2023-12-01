number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
number_three = int(input("Enter the third number: "))

minimum = 0
maximum = 0

if number_one < number_two:
    if number_one < number_three:
        minimum = number_one

if number_two < number_one:
    if number_two < number_three:
        minimum = number_two

if number_three < number_two:
    if number_three < number_one:
        minimum = number_three

print("The smallest number is ", minimum)

if number_one > number_two:
    if number_one > number_three:
        maximum = number_two

if number_two > number_one:
    if number_two > number_three:
        maximum = number_two

if number_three > number_two:
    if number_three > number_one:
        maximum = number_three
print('The largest number is ', maximum)
