from unittest import TestCase

from class_practice.function import add_to_ending_of_string


class TestAddToEndOfAString(TestCase):
    def test_add_string_to_string_length_equal_to_3(self):
        sample_input = 'abc'
        result = 'abcing'
        self.assertEqual(result, add_to_ending_of_string.add_to_string_length_equal_to_three(sample_input))

    def test_add_ly_to_string_if_already_end_with_ing(self):
        sample_input = 'sting'
        result = 'stingly'
        self.assertEqual(result, add_to_ending_of_string.add_ly_to_string_if_already_end_with_ing(sample_input))

    def test_add_ly_to_string_if_already_end_with_ing2(self):
        sample_input = 'sting'
        result = 'stingly'
        self.assertEqual(result, add_to_ending_of_string.add_ly_to_string_if_already_end_with_ing(sample_input))

    def test_string_less_than_3(self):
        sample_input = 'it'
        result = 'it'
        self.assertEqual(sample_input, result)
