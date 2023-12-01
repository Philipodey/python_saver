for row in range(20):
    # print()
    for column in range(1 + row):
        print("*", end="")
    for a in range(row, 20):
        print(" ", end="")
    for column in range(row, 20):
        print("*",end="")
    for j in range(row-1):
        print(" ", end="")
    for q in range(row-1):
        print(" ", end="")
    for p in range(row, 20):
        print("*", end="")
    for s in range(1 + row):
        print(" ", end="")
    print()
