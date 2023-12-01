# basket = []
# basket.append("shirt")
# basket.append(40)
# print(basket)
# basket.append("cap")
# print(basket)
# print(basket[0])
# print(basket[1])
# print(basket[2])
# # to print len you can just print
# basket_length = len(basket)
# print(basket_length)
# # How to access the values in a list
# # print(basket[-2:-1])
# for value in basket:
#     print(value, end="\t")

numbers = int(input("Enter the number of elements: "))
my_list = []
add = 0
average = 0
minimum = 0
maximum = 0

for count in range(1, numbers):
    scores = int(input(f"Enter the elements {count}: "))
    my_list.append(scores)
    add = add + scores
    if count < numbers:
        minimum = count


average = add / count
print(average)
print(add)
print("scores:", my_list)
print(my_list)
print(minimum)
