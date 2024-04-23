from assignment.bank.exceptions.invalid_account_number_exception import InvalidAccountNumberError
from assignment.bank.server_class import Account
from assignment.bank.server_class.Account import *


class Bank:
    def __init__(self):
        self.list_of_accounts = []
        self.total_number_of_account = 0

    def create_account_for(self, first_name, last_name, pin) -> Account:
        self.get_size_of_account_list()
        account_number = self.generate_account_number()
        account_name: str = self._generate_account_name(first_name, last_name)
        account_create_list: Account = Account(account_number, pin, account_name)
        self.total_number_of_account += 1
        self.list_of_accounts.append(account_create_list)
        return account_create_list

    def generate_account_number(self) -> str:
        return str(234 + (len(self.list_of_accounts) + 1))

    def get_size_of_account_list(self) -> int:
        return len(self.list_of_accounts)

    def _generate_account_name(self, first_name, last_name) -> str:
        return first_name + " " + last_name

    def deposit(self, account_number: str, amount: float):
        account_number = self.find_account(account_number)
        account_number.deposit(amount)

    def find_account(self, account_number: str) -> Account:
        for account in self.list_of_accounts:
            if account_number == account.get_account_number():
                return account
            else:
                raise InvalidAccountNumberError("account does not exist!!!")

    def check_balance(self, account_number: str, pin: str):
        find_account_number = self.find_account(account_number)
        return find_account_number.check_balance(pin)
