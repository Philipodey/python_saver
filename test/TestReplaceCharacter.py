from unittest import TestCase

from class_practice.function.ReplaceCharacter import replace_string


class TestReplaceCharacter(TestCase):
    def test_replace_character_except_first_character(self):
        word = 'restart'
        old_string = 'r'
        new_string = '$'
        self.assertEqual('resta$t', replace_string(word, old_string, new_string))
