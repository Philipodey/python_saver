number = int(input("Enter the binary digit: "))
# number = newNumber
turnNumber = 0
digit = 0
count = 1
while number != 0:
    digit = number % 10
    turnNumber = (turnNumber + digit) / 2
    number = number // 10
print(turnNumber)

