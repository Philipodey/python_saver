# number = int(input("Enter a number :"))
largest = 0
smallest =0
add = 0
average = 1
product = 1
for count in range(1, 5):
    least = smallest
    count += count
    number = int(input("Enter a number : "))
    add += number
    average = add / count
    product *= number
    if number > largest:
        largest = number
    else:
        least = number
    # count += 1
print(f"""
        The sum of the numbers is {add}
    The average of the number is {average}
    The product of the number are {product}
    The smallest of the number is {least}
    The largest of the number is {largest}
""")
