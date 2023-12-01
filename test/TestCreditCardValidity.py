from unittest import TestCase

import credit_card_validity


class TestCreditCardValidity(TestCase):
    def testThatTheNumberIsBetween13And16(self):
        cardNumber = ["4", "3", "8", "8", "5", "7", "6", "0", "1", "8", "4", "0", "3", "3"]
        expected = credit_card_validity.credit_card_number(cardNumber)
        result = "Visa card"
        self.assertEqual(expected, result)

    def testThatTheCardNumberValidity(self):
        card_number = ["4", "3", "8", "8", "5", "7", "6", "0", "1", "8", "4", "1", "0", "7", "0", "7"]
        expected = credit_card_validity.credit_card_validate(card_number)
        result = "Valid"
        self.assertEqual(expected, result)
