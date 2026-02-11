class BankingError(Exception):
    def __init__(self, message="Banking error"):
        super().__init__(message)


class AuthenticationError(BankingError):
    pass


class CardBlockedError(BankingError):
    pass


class InsufficientFundsError(BankingError):
    pass


class InsufficientATMCashError(BankingError):
    pass


class InvalidAmountError(BankingError):
    pass
