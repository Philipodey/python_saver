from unittest import TestCase
from listFunction.function import dictionary_sort


class TestDictionaryMethods(TestCase):
    def test_that_key_values_can_be_added_to_dictionary(self):
        diction = {0: 10, 1: 20}
        item_pair = {2: 30}
        result = {0: 10, 1: 20, 2: 30}
        expected = dictionary_sort.add_to_dictionary(diction, item_pair)
        self.assertEqual(result, expected)

    # def test_
