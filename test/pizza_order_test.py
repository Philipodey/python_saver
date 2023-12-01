from unittest import TestCase
from listFunction.function import pizza_order


class TestPizzaOrder(TestCase):
    def test_pizza_size(self):
        size = "large"
        result = 10
        expected = pizza_order.box_size(size)
        self.assertEqual(expected, result)

    def test_number_of_people(self):
        super_hungry = 3
        hungry = 3
        classic = 2
        expected = pizza_order.number_of_people_in_party(super_hungry, hungry, classic)
        self.assertEqual(expected, 23)

    def test_number_of_box_to_buy(self):
        size = "LARGE"
        size_to_buy = pizza_order.box_size(size)
        super_hungry = 3
        hungry = 3
        classic = 2
        # people_available = pizza_order.number_of_people_in_party(super_hungry, hungry, classic)
        expected = pizza_order.number_of_box_to_buy(super_hungry, hungry, classic, size)
        self.assertEqual(3, expected)

    def test_pieces_of_pizza_remaining(self):
        super_hungry = 3
        hungry = 3
        classic = 2
        size = "Large"
        result = 7
        number_of_pizza_remainder = pizza_order.pieces_of_pizza_remain(super_hungry, hungry, classic, "Large")
        self.assertEqual(result, number_of_pizza_remainder)

    def test_number_of_people_in_the_party(self):
        super_hungry = 3
        hungry = 3
        classic = 2
        size = "Large"
        result = 15000.0
        total_amount_for_pizza = pizza_order.total_amount_of_pizza(super_hungry, hungry, classic, size)
        self.assertEqual(result, total_amount_for_pizza)
