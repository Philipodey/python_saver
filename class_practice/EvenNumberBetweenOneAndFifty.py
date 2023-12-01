def even_number(number):
    counter = 0
    for count in number:
        count += 1
        print(count, end=" ")
        counter += 1
    print("\n")
    print(counter)
    print(count)
    average = count / counter
    print(average)


even_number(range(0, 50, 2))
