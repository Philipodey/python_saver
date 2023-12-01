from unittest import TestCase
from class_practice.function import list_to_dictionary
from class_practice.function.list_to_dictionary import difference, dictionary_get, split_list, list_to_dictionary, \
    list_to_dictionary2


class TestListToDictionary(TestCase):
    def test_smallest_and_largest(self):
        sample_list = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        result = 70
        self.assertEqual(result, difference(sample_list))

    def test_dictionary_get(self):
        input1 = ['a', 'b', 'c', 'd', 'e']
        input2 = [1, 2, 3, 4, 5]
        result = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(result, dictionary_get(input1, input2))

    def test_split_list(self):
        input1 = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        result = [10, 75, 20, 30, 15], [5, 40, 25, 40, 35]
        self.assertEqual(result, split_list(input1))

    def test_list_to_dictionary(self):
        sample_input = ['apple', 'banana', 'coconut', 'calender']
        result = {'a': 'apple', 'b': 'banana', 'c': 'coconut', 'C': 'calender'}
        self.assertEqual(result, list_to_dictionary2(sample_input))
