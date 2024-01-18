from assignment.bank.exceptions.insufficient_funds_Exception import InsufficientFundsError
from assignment.bank.exceptions.invalid_amount_error import InvalidAmountError
from assignment.bank.exceptions.invalid_pin_error import InvalidPinError


class Account:
    __balance = 0

    def __init__(self, account_number: str, pin: str, account_name: str):
        self.__account_number = account_number
        self.__pin = pin
        self.__name = account_name

    def deposit(self, amount):
        if amount < 0:
            raise InvalidAmountError("Invalid deposit amount\nTry depositing a valid amount amount greater #0.00Naira")
        self.__balance += amount

    def check_balance(self, pin) -> float:
        self._invalid_pin_exception(pin)
        return self.__balance

    def withdraw(self, pin: str, amount: float):
        self._invalid_pin_exception(pin)
        self._invalid_amount_exception(amount)
        self._insufficient_funds_exception(amount)
        self.__balance -= amount

    def _invalid_pin_exception(self, pin):
        if self.__pin != pin:
            raise InvalidPinError("Invalid withdrawal pin!!!\nTry using the appropriate pin to transfer")

    def _invalid_amount_exception(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Invalid withdrawal amount\nTry withdrawing amount greater than 0.00Naira")

    def get_account_number(self) -> str:
        return self.__account_number

    def _insufficient_funds_exception(self, amount):
        if self.__balance < amount:
            raise InsufficientFundsError("Insufficient funds!!\nPlease input a valid amount to withdraw")

    def __str__(self):
        print(f"""
        ==========================================
            The account name is {self.__name}
            The account number is {self.__account_number}
            The balance is {self.__balance}
            Your father wan know my pin abi!!! 
        =========================================
        
        """)
