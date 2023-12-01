number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

largest = 0
if number1 > number2:
   if number1 > number3:
       largest = number1

if number2 > number1:
    if number2 > number3:
        largest = number2

if number3 > number1:
    if number3 > number2:
        largest = number3

print("The largest is ", +largest)
