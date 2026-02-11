from transaction import Transaction, TransactionType
from atm_errors import *


class BankAccount:
    def __init__(self, account_number: int):
        if account_number <= 0:
            raise BankingError("Account number must be positive")
        self.account_number = account_number
        self._balance = 0
        self._transactions: list[Transaction] = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        self._balance += amount
        self.add_transaction(Transaction(TransactionType.DEPOSIT, amount))

    def withdraw(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        if amount > self._balance:
            raise InsufficientFundsError("Insufficient amount")
        self._balance -= amount
        self.add_transaction(Transaction(TransactionType.WITHDRAW, amount))

    @property
    def balance(self) -> float:
        return self._balance

    def add_transaction(self, transaction: Transaction):
        self._transactions.append(transaction)

    def get_transaction_history(self) -> list[Transaction]:
        return list(self._transactions)
