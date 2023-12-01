numbers = [15, 20, 25, 20, 10, 5]
smallest_one = numbers[5]
print(smallest_one)

smallest = numbers[0]

for count in numbers:
    if count < smallest:
        smallest = count

print(smallest)
