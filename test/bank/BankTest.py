import unittest

from assignment.bank.server_class.Account import Account
from assignment.bank.server_class.bank import Bank


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # gtb: Account = Account("Odey","1","12")
        self.first_bank = Bank()

    def test_bank_can_create_one_account(self):
        first_customer = self.first_bank.create_account_for("Philip", "Odey", "pin")
        account: Account = Account("2341", "pin", "Philip odey")
        self.assertEqual(1, self.first_bank.get_size_of_account_list())

    def test_bank_can_create_multiple_account(self):
        first_customer = self.first_bank.create_account_for("Philip", "Odey", "pin")
        account: Account = Account("2341", "pin", "Philip odey")
        self.assertEqual(1, self.first_bank.get_size_of_account_list())
        second_customer = self.first_bank.create_account_for("Martina", "Odey", "4444")
        account1: Account = Account("2342", "pin", "Philip Odey")
        self.assertEqual(2, self.first_bank.get_size_of_account_list())

    def test_check_account_number(self):
        first_customer = self.first_bank.create_account_for("Philip", "Odey", "pin")
        account: Account = Account("2341", "pin", "Philip odey")
        self.assertEqual("2341", account.get_account_number())

    def test_find_account(self):
        self.first_bank.create_account_for("Philip", "Odey", "pin")
        number = "2341"
        account: Account = Account(number, "pin", "Philip odey")
        account_number = self.first_bank.find_account(number)
        print(account_number)
        self.assertIs("2341", account.get_account_number())

    def test_that_account_can_deposit(self):
        first_customer = self.first_bank.create_account_for("Philip", "Odey", "pin")
        account: Account = Account("2341", "pin", "Philip odey")
        self.first_bank.deposit("2341", 2500.00)
        self.assertEqual(2500, self.first_bank.check_balance("1", "2341"))
