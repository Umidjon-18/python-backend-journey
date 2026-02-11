from datetime import datetime
from transaction_type import TransactionType


class Transaction:
    def __init__(self, type: TransactionType, amount: float):
        self.type = type
        self.amount = amount
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Transaction(type={self.type}, amount={self.amount}, time={self.timestamp})"
