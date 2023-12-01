from listFunction.function import pizza_order
from listFunction.function.pizza_order import box_size, number_of_people_in_party, number_of_box_to_buy, \
    pieces_of_pizza_remain, total_amount_of_pizza

size = input("Enter the size of pizza you desire: ")
super_hungry = int(input("Enter the number of super hungry: "))
hungry = int(input("Enter the number of hungry individual present: "))
classic = int(input("Enter the number of classic individual present: "))

pizza_box_size = box_size(size)
number_of_people_present_in_the_party = number_of_people_in_party(super_hungry, hungry, classic)
number_of_boxes_to_buy = number_of_box_to_buy(super_hungry, hungry, classic, size)
pizza_remainder = pieces_of_pizza_remain(super_hungry, hungry, classic, size)
amount_to_pay = total_amount_of_pizza(super_hungry, hungry, classic, size)

print(f"""
********************************************
Your desired pizza size is {size}
The number of  people present is {number_of_people_present_in_the_party}
The number of boxes you need to buy is {number_of_boxes_to_buy}
The remainder of pizza is {pizza_remainder}
The amount you need to pay is {amount_to_pay}
*******************************************
""")


