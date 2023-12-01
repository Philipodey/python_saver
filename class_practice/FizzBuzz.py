# for count in range(1, 50):
#     if count % 3 == 0 and count % 5 == 0:
#         print("FizzBuzz")
#     elif count % 3 == 0:
#         print("Fizz")
#     elif count % 5 == 0:
#         print("Buzz")
#     else:
#         print(count)
def fizz_buzz(number):
    count = 1
    while count < number:
        if count % 3 == 0 and count % 5 == 0:
            print("FizzBuzz")
        elif count % 3 == 0:
            print("Fizz")
        elif count % 5 == 0:
            print("Buzz")
        else:
            print(count)
        count += 1


(fizz_buzz(50))
