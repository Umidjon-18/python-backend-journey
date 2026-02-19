from atm import ATM
from bank_account import BankAccount
from card import Card


def run():
    # Create account
    account = BankAccount(account_number=1001)
    account.deposit(1000)

    # Create card
    card = Card(card_number="1234-5678-9999-0000", pin="1234", account=account)

    # Create ATM
    atm = ATM(cash_available=5000)

    print("Insert card")
    atm.insert_card(card)

    print("Authenticate")
    atm.authenticate("1234")

    print("Withdraw 300")
    atm.withdraw(300)

    print("Balance:", atm.check_balance())

    print("Eject card")
    atm.eject_card()

    print("\nTransaction history:")
    for tx in account.get_transaction_history():
        print(tx)


if __name__ == "__main__":
    run()
