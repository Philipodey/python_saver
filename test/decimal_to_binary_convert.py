from unittest import TestCase

from listFunction.function import decimal_to_binary


class TestDecimalToBinaryConvert(TestCase):
    def test_decimal_to_binary(self):
        number = 278
        result = "100010110"
        expected = decimal_to_binary.decimal_to_binary(number)
        self.assertEqual(result, expected)

    def test_binary_to_decimal(self):
        number = 100010110
        result = 278
        expected = decimal_to_binary.binary_to_decimal(number)
        self.assertEqual(expected, result)
