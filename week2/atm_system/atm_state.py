from abc import ABC


class ATMState(ABC):
    pass


class IdleState(ATMState):
    pass


class CardInsertedState(ATMState):
    pass


class AuthenticatedState(ATMState):
    pass
