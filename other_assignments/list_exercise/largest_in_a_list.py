numbers = [15, 20, 25, 20, 10, 5]
largest = numbers[2]
print(largest)

largest_one = 0

for count in numbers:
    if count > largest_one:
        largest_one = count

print(largest_one)
