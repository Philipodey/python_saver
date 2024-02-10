from unittest import TestCase

from assignment import count_character


class TestNumberCount(TestCase):
    def test_number_count_in_a_list(self):
        input = "semicolon.africa"
        output = {"s": 1, "e": 1, "m": 1, "i": 2, "c": 2, "o": 2, "l": 1, "n": 1, ".": 1, "a": 2, "f": 1, "r": 1}
        expected = count_character.count_character_in_list(input)
        self.assertEqual(output, expected)
