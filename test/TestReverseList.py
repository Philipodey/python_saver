from unittest import TestCase
import tuple_assignment


class TestReverseList(TestCase):
    def test_reverse_tuple(self):
        numbers = (10, 20, 30, 40, 50)
        expected = tuple_assignment.turn_tuple(numbers)
        result = (50, 40, 30, 20, 10)
        self.assertEqual(expected, result)

    def test_remove_element(self):
        numbers = ("Orange", [10, 20, 30], (5, 15, 25))
        expected = tuple_assignment.remove_element(numbers)
        result = ((0, 20), (1, 25))
        self.assertEqual(expected, result)

    def test_element_unpacking(self):
        numbers = 15, 25, 60, 50, 30, 40, 45, 55
        expected = tuple_assignment.unpack_element(numbers)
        result = (55, 15)
        self.assertEqual(result, expected)

    def test_more_numbers_that_appear_more_than_once(self):
        numbers = 20, 10, 15, 20, 5, 30, 10, 35, 10, 40, 45, 5
        result = 5, 10, 20
        expected = tuple_assignment.appear_twice(numbers)
        self.assertEqual(result, expected)
