# print('number\tsquare\tcube')
# for count in range (11):
#     print(f"{count:>4}\t{count*count:>4}\t{count*count*count:^3}")

print('number\tsquare\tcube')

count = 1
while count <= 10:
    print(f"{count:>4}\t{count **2:>4}\t{count ** 3:^3}")
    count += 1