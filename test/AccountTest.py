from unittest import TestCase

from assignment.bank.Account import Account
from assignment.bank.exceptions.invalid_amount_error import InvalidAmountError


class AccountTest(TestCase):

    def test_deposit_to_account(self):
        balance = 0.0
        account_number = "1"
        gtb: Account = Account(balance, account_number, "1234")
        amount: float = 2000.00
        gtb.deposit(amount)
        self.assertEqual(2000.00, gtb.check_balance())

    def test_account_raises_an_exception_when_amount_to_deposit_is_less_than_0(self):
        balance = 0.0
        account_number = "1"
        gtb: Account = Account(balance, account_number, "1234")
        with self.assertRaises(InvalidAmountError):
            gtb.deposit(-10.00)

    def test_account_raises_an_exception_when_amount_to_deposit_is_less_than_0_and_check_balance(self):
        balance = 0.0
        account_number = "1"
        gtb: Account = Account(balance, account_number, "1234")
        with self.assertRaises(InvalidAmountError):
            gtb.deposit(-10.00)
        self.assertEqual(0.0, gtb.check_balance())

    def test_account_can_withdraw(self):
        balance = 0.0
        account_number = "1"
        gtb: Account = Account(balance, account_number,"1234")
        gtb.deposit(2000.00)
        gtb.withdraw("1234", 2000.00)
        self.assertEqual(0.0, gtb.check_balance())

    def test_account_can_not_withdraw_amount_less_than_zero(self):
        balance = 2000.0
        account_number = "1"
        gtb: Account = Account(balance, account_number, "1234")
        with self.assertRaises(InvalidAmountError):
            gtb.withdraw("1234", -0)
        self.assertEqual(2000.0, gtb.check_balance())



