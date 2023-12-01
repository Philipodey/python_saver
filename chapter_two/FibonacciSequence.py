add_one = 0
add_two = 1
add = add_one + add_two
for count in range(50):
    print(add_one, end=' ')
    add_one = add_two
    add_two = add
    add = add_one + add_two
    if add_one > 50:
        break
print()

add_one = 1
add_two = 0
add = add_one + add_two
while add_two < 50:
    print(add_two, end=' ')
    add_one = add_two
    add_two = add
    add = add_two + add_one
