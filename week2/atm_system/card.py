from bank_account import BankAccount
from atm_errors import *


class Card:
    def __init__(self, card_number: str, pin: str, account: BankAccount):
        if len(pin.strip()) != 4:
            raise BankingError("Pincode must be 4 length long")
        self.card_number = card_number
        self._pin = pin
        self.account = account
        self.is_blocked = False
        self.failed_attempts = 0

    def check_pin(self, value: str):
        if self.is_blocked:
            raise CardBlockedError("Card is blocked")
        if self._pin == value:
            self.failed_attempts = 0
        else:
            self.failed_attempts += 1
            if self.failed_attempts == 3:
                self.block_card()
                raise CardBlockedError("Card is blocked")

    def block_card(self):
        self.is_blocked = True
