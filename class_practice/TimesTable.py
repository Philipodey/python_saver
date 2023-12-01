def time_table(number_one, number_two):
    for row in number_one:
        for column in number_two:
            print(f"{column:>3} *{row:>3} = {row * column:^2}\t", end=" ")
        print("")


time_table(range(1, 13), range(2, 21))
