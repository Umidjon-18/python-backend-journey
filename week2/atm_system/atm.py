from typing import Optional
from card import Card
from atm_errors import *
from atm_state import *


class ATM:
    def __init__(self, cash_available: float):
        self.cash_available = cash_available
        self.current_card: Optional[Card] = None
        self.state: ATMState = IdleState()

    def insert_card(self, card: Card):
        if self.state is CardInsertedState:
            raise BankingError("Card is already inserted")
        if card.is_blocked:
            raise CardBlockedError("Card is blocked")
        self.current_card = card

    def authenticate(self, pin: str):
        if self.state is IdleState:
            raise ("Please enter the card first")
        if self.current_card.check_pin(pin):
            self.state = AuthenticatedState()
        else:
            self.state = IdleState()

    def withdraw(self, amount: float):
        if self.current_card is None:
            raise BankingError("Card is not inserted")
        if not self.state is AuthenticatedState:
            raise AuthenticationError("Please authenticate first")
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        if amount > self.cash_available:
            raise InsufficientATMCashError("Insufficient cash")
        self.current_card.account.withdraw(amount)
        self.cash_available -= amount

    def deposit(self, amount: float):
        if self.current_card is None:
            raise BankingError("Card is not inserted")
        if not self.state is AuthenticatedState:
            raise AuthenticationError("Please authenticate first")
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        self.current_card.account.deposit(amount)

    def check_balance(self) -> float:
        if self.state is IdleState:
            raise BankingError("Card is not inserted")
        if not self.state is AuthenticatedState:
            raise AuthenticationError("Please authenticate first")
        return self.current_card.account.balance

    def eject_card(self):
        self.current_card = None
        self.state = IdleState()
