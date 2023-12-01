import unittest

from listFunction.function.ListFunction import largest, reverse_element, element_exit, element_on_odd_position, \
    commute_total_of_all_element, string_is_palindrome, concatenate_two_lists


class MyTestCase(unittest.TestCase):
    def test_largest(self):
        number = {45, 76, 23, 45, 98}
        maximum = 98
        result = largest(number)
        self.assertEqual(maximum, result)  # add assertion here

    def test_reverse_element(self):
        number = [45, 67, 23, 12]
        reverse = [12, 23, 67, 45]
        result = reverse_element(number)
        self.assertEqual(result, reverse)

    def test_element_exit(self):
        number = [45, 65, 87, 23, 27]
        element = 87
        result = element_exit(number, element)
        self.assertTrue(result)

    def test_element_on_odd_position(self):
        number = [56, 76, 23, 12, 87, 34]
        elements = [76, 12, 34]
        result = element_on_odd_position(number)
        self.assertEqual(result, elements)

    def test_total_of_all_element(self):
        number = [56, 3, 1, 4, 7, 3, 3]
        total = 77
        result = commute_total_of_all_element(number)
        self.assertEqual(result, total)

    def test_that_string_is_palindrome(self):
        character = "dod"
        result = string_is_palindrome(character)
        self.assertTrue(result)

    def test_concatenate_two_lists(self):
        first_list = ["d", "a", "d"]
        second_list = [1, 2, 3, 4]
        concatenate = ["d", "a", "d", 1, 2, 3, 4]
        result = concatenate_two_lists(first_list, second_list)
        self.assertEqual(result, concatenate)

    def test_concatenate_two_lists_alternatively(self):
        first_list = ["d", "a", "d"]
        second_list = [1, 2, 3, 4]
        concatenate = ["d", "a", "d", 1, 2, 3, 4]
        result = concatenate_two_lists(first_list, second_list)
        self.assertEqual(result, concatenate)
