from assignment.bank.exceptions.invalid_amount_error import InvalidAmountError


class Account:

    def __init__(self, balance: float, account_number: str, pin: str):
        self.balance = balance
        self.account_number = account_number
        self.pin = pin

    def deposit(self, amount):
        if amount < 0:
            raise InvalidAmountError("Invalid deposit amount\nTry depositing a valid amount amount greater #0.00Naira")
        self.balance += amount

    def check_balance(self) -> float:
        return self.balance

    def withdraw(self, pin: str, amount: float):
        if pin.__eq__(self.pin):
            if amount <= 0:
                raise InvalidAmountError("Invalid withdrawal amount\nTry withdrawing amount greater than 0.00Naira")
            self.balance -= amount
