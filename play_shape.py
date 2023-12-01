
for row in range(0, 8):
    print()
    for column in range(0, row-1):
        print('*', end="")
for row in range(0, 8):
    print()
    for column in range(5-row):
        print("*", end="")
