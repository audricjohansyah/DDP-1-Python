class User:
    def __init__(self, balance, bank_account):
        self.balance = balance
        self.bank_account = bank_account

    def get_balance(self):
        return self.balance

    def get_bank_account(self):
        return self.bank_account

    def add_amount_to_balance(self, amount):
        self.balance += amount

    def transfer_to(self, another_user, amount):
        if (self == another_user):
            print("Tidak bisa transfer ke diri sendiri")
            return

        if (self.get_bank_account().get_name() != another_user.get_bank_account().get_name()):
            if (self.get_balance() < (amount + 6500)):
                print("Balance tidak cukup")
                return
            self.balance -= (amount + 6500)
            another_user.add_amount_to_balance(amount)
        else:
            if (self.get_balance() < amount):
                print("Balance tidak cukup")
                return
            another_user.add_amount_to_balance(amount)
            self.balance -= amount

    def updateBalance(self, amount_of_month):
        if (self.get_bank_account().get_interest() > 0):
            self.balance += int(self.balance * self.get_bank_account().get_interest() * amount_of_month)