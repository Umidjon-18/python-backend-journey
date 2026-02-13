from abc import ABC, abstractmethod
from atm import *


class ATMState(ABC):

    def __init__(self, atm: ATM):
        self.atm = atm

    def insert_card(self, card):
        return NotImplementedError

    def authenticate(self, pin: str):
        return NotImplementedError

    def withdraw(self, amount: float):
        return NotImplementedError

    def deposit(self, amount: float):
        return NotImplementedError

    def check_balance(self):
        return NotImplementedError

    def eject_card(self):
        return NotImplementedError


class IdleState(ATMState):
    pass


class CardInsertedState(ATMState):
    pass


class AuthenticatedState(ATMState):
    pass
