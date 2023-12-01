from unittest import TestCase

from class_practice.Accounts import Account


class TestAccount (TestCase):
    def test_That_Account_Can_Deposit_Money(self):
        savings_Account = Account()