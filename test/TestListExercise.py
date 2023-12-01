from unittest import TestCase
import list_exercise


class TestListExercise(TestCase):
    def test_multiplication_function(self):
        expected = list_exercise.multiply_all_numbers_by_three([3, 7, 2, 6, 5])
        self.assertEqual(expected, [27, 343, 8, 216, 125])
