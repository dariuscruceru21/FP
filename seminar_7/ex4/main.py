from ex4.account import Account
from ex4.test import test_cash_out

test_cash_out()

def main():
    bankAccount = Account('23', 'Darius')
    bankAccount.cash_in(1000000000)
    print(bankAccount.sum)

main()
