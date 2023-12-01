constant = 4
pi = 0.00
counter = 1
for count in range(1, 500000, 2):
    counter += 1
    if counter % 2 == 0:
        pi += (constant / count)
    else:
        pi += -(constant / count)

print(f"{pi}")

