from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from card import Card
from atm_errors import *

if TYPE_CHECKING:
    from atm import ATM


class ATMState(ABC):

    def __init__(self, atm: "ATM"):
        self.atm = atm

    @abstractmethod
    def insert_card(self, card):
        pass

    @abstractmethod
    def authenticate(self, pin: str):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def eject_card(self):
        pass


class IdleState(ATMState):
    def __init__(self, atm):
        super().__init__(atm)

    def insert_card(self, card: Card):
        if card.is_blocked:
            raise CardBlockedError("Card is blocked")
        self.atm.current_card = card
        self.atm.set_state(CardInsertedState(self.atm))

    def authenticate(self, pin: str):
        raise BankingError("Please enter the card first")

    def withdraw(self, amount: float):
        raise BankingError("Please enter the card first")

    def deposit(self, amount: float):
        raise BankingError("Please enter the card first")

    def check_balance(self) -> float:
        raise BankingError("Please enter the card first")

    def eject_card(self):
        raise BankingError("Please enter the card first")


class CardInsertedState(ATMState):
    def __init__(self, atm):
        super().__init__(atm)

    def insert_card(self, card: Card):
        raise BankingError("Card is already inserted")

    def authenticate(self, pin: str):
        if self.atm.current_card.is_blocked:
            raise CardBlockedError("Card is blocked")

        if self.atm.current_card.check_pin(pin):
            self.atm.set_state(AuthenticatedState(self.atm))
        else:
            raise AuthenticationError("Incorrect pincode")

    def withdraw(self, amount: float):
        raise AuthenticationError("Please authenticate first")

    def deposit(self, amount: float):
        raise AuthenticationError("Please authenticate first")

    def check_balance(self) -> float:
        raise AuthenticationError("Please authenticate first")

    def eject_card(self):
        self.atm.current_card = None
        self.atm.set_state(IdleState(self.atm))


class AuthenticatedState(ATMState):
    def __init__(self, atm):
        super().__init__(atm)

    def insert_card(self, card: Card):
        raise BankingError("Card is already inserted")

    def authenticate(self, pin: str):
        raise BankingError("Already authenticated")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        if amount > self.atm.cash_available:
            raise InsufficientATMCashError("Insufficient cash")
        self.atm.current_card.account.withdraw(amount)
        self.atm.cash_available -= amount

    def deposit(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        self.atm.current_card.account.deposit(amount)

    def check_balance(self) -> float:
        return self.atm.current_card.account.balance

    def eject_card(self):
        self.atm.current_card = None
        self.atm.set_state(IdleState(self.atm))
