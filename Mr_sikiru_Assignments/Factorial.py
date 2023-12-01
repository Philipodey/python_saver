number = int(input("Enter a number: "))
factorial = 1
count = 1
for count in range(number):
    count += 1
    factorial *= count
print(f"The factorial of {number} is {factorial}")
