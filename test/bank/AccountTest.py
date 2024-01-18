from unittest import TestCase

from assignment.bank.exceptions.insufficient_funds_Exception import InsufficientFundsError
from assignment.bank.server_class.Account import Account
from assignment.bank.exceptions.invalid_amount_error import InvalidAmountError
from assignment.bank.exceptions.invalid_pin_error import InvalidPinError


class AccountTest(TestCase):

    def test_deposit_to_account(self):
        account_number = "1"
        gtb: Account = Account(account_number, "1234", "Odey Philip")
        amount: float = 2000.00
        gtb.deposit(amount)
        self.assertEqual(2000.00, gtb.check_balance("1234"))

    def test_account_raises_an_exception_when_amount_to_deposit_is_less_than_0(self):
        balance = 0.0
        account_number = "1"
        gtb: Account = Account(account_number, "1234", "Odey Philip")
        with self.assertRaises(InvalidAmountError):
            gtb.deposit(-10.00)

    def test_account_raises_an_exception_when_amount_to_deposit_is_less_than_0_and_check_balance(self):
        account_number = "1"
        gtb: Account = Account(account_number, "1234", "Odey philip")
        with self.assertRaises(InvalidAmountError):
            gtb.deposit(-10.00)
        self.assertEqual(0.0, gtb.check_balance("1234"))

    def test_account_can_withdraw(self):
        account_number = "1"
        gtb: Account = Account(account_number,"1234", "odey")
        gtb.deposit(2000.00)
        gtb.withdraw("1234", 2000.00)
        self.assertEqual(0.0, gtb.check_balance("1234"))

    def test_account_can_not_withdraw_amount_less_than_zero(self):
        balance = 2000.0
        account_number = "1"
        gtb: Account = Account(account_number, "1234", "odey Philip")
        gtb.deposit(balance)
        with self.assertRaises(InvalidAmountError):
            gtb.withdraw("1234", -0)
        self.assertEqual(2000.0, gtb.check_balance("1234"))

    def test_withdraw_account_with_the_wrong_pin_raise_exception(self):
        account_number = "1"
        gtb: Account = Account(account_number, "1234", "odey")
        with self.assertRaises(InvalidPinError):
            gtb.withdraw("1235", 2000.00)

    def test_check_balance_with_the_wrong_pin(self):
        account_number = "1"
        gtb: Account = Account(account_number, "1234", "odey")
        with self.assertRaises(InvalidPinError):
            gtb.check_balance("1235")

    def test_withdraw_amount_greater_than_balance_raise_exception(self):
        gtb: Account = Account("1", "1234", "Odey Philip")
        gtb.deposit(1500.00)
        with self.assertRaises(InsufficientFundsError):
            gtb.withdraw("1234", 3000.00)


