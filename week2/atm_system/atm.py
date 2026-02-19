from typing import Optional
from card import Card
from atm_state import ATMState, IdleState


class ATM:
    def __init__(self, cash_available: float):
        self.cash_available = cash_available
        self.current_card: Optional[Card] = None
        self.state: ATMState = IdleState(self)

    def insert_card(self, card: Card):
        return self.state.insert_card(card)

    def authenticate(self, pin: str):
        return self.state.authenticate(pin)

    def withdraw(self, amount: float):
        return self.state.withdraw(amount)

    def deposit(self, amount: float):
        return self.state.deposit(amount)

    def check_balance(self) -> float:
        return self.state.check_balance()

    def eject_card(self):
        return self.state.eject_card()

    def set_state(self, state: ATMState):
        self.state = state
