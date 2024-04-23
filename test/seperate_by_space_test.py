from unittest import TestCase

from Task import seperate_by_space


class TestSeperateBySpace(TestCase):
    def test_seperate_string_by_space(self):
        sample_input_1 = "abc"
        sample_input_2 = "def"
        result = 'abc def'
        self.assertEqual(result, seperate_by_space.seperate_strings(sample_input_1, sample_input_2))

    def test_seperate_more_than_two_string_by_space(self):
        sample_input_1 = "abc"
        sample_input_2 = "def"
        sample_input_3 = "defdfvs"
        sample_input_4 = "deffgda"
        result = 'abc def defdfvs deffgda'
        self.assertEqual(result,
                         seperate_by_space.seperate_strings(sample_input_1,
                                                            sample_input_2,
                                                            sample_input_3,
                                                            sample_input_4))
