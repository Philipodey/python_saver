numbers = [15, 20, 25, 20, 10, 5]
arranged_list = []

for count in numbers:
    if count not in arranged_list:
        arranged_list.append(count)
print(arranged_list)
