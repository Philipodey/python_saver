from unittest import TestCase

from Task import double_number_in_a_list


class TestDoubleNumberInAList(TestCase):

    def test_double_number_in_a_list(self):
        number = "2, 3, 5"
        result = [4, 9, 25]
        expected = double_number_in_a_list.double_number_in_list(number)
        self.assertEqual(expected, result)
