def box_size(size: str):
    pizza_boxes = {"SMALL": 4, "MEDIUM": 6, "LARGE": 10}
    size = size.upper()
    if size in pizza_boxes.keys():
        return int(pizza_boxes.get(size))


def number_of_people_in_party(super_hungry, hungry, classic):
    different_people = 0
    if super_hungry >= 0 and hungry >= 0 and classic >= 0:
        different_people = (super_hungry * 4) + (hungry * 3) + (classic * 1)

    return different_people


def number_of_box_to_buy(super_hungry, hungry, classic, size):
    people_available = number_of_people_in_party(super_hungry, hungry, classic)
    size_to_buy = box_size(size)
    number_of_box = int(people_available) // size_to_buy
    if number_of_box % size_to_buy != 0 or number_of_box < 0:
        number_of_box = number_of_box + 1

    return number_of_box


def pieces_of_pizza_remain(super_hungry, hungry, classic, size):
    people_available = number_of_people_in_party(super_hungry, hungry, classic)
    number_of_box = number_of_box_to_buy(super_hungry, hungry, classic, size)
    pizza_box_size = box_size(size)
    box_available_in_excess = pizza_box_size * number_of_box
    pieces_of_pizza_remaining = box_available_in_excess - people_available
    if pieces_of_pizza_remaining < 0:
        number_of_box += 1
        box_available_in_excess = pizza_box_size * number_of_box
        pieces_of_pizza_remaining = box_available_in_excess - people_available
    return pieces_of_pizza_remaining


def total_amount_of_pizza(super_hungry: int, hungry: int, classic: int, size: str):
    prize = 0
    pizza_box = {"SMALL": 1200.00, "MEDIUM": 3000.00, "LARGE": 5000.00}
    size = size.upper()
    number_of_boxes_to_buy = number_of_box_to_buy(super_hungry, hungry, classic, size)
    if size in pizza_box.keys():
        prize = float(pizza_box.get(size) * number_of_boxes_to_buy)
    return prize
