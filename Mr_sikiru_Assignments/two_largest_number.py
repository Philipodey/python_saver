number = int(input("Enter any number: "))
count = 1
largest = number
second_largest = 0
for count in range(3):
    number = int(input("Enter any number: "))
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number
print(f"The first largest is {largest}")
print(f"THe second largest number is {second_largest}")
