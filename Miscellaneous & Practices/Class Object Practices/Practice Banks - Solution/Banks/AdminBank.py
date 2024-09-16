from User import User

class AdminBank(User):
    def __init__(self, bank):
        self.bank_account = bank

    def transfer_to(self, another_user, amount):
        if (self == another_user):
            print("Tidak bisa transfer ke diri sendiri")
            return

        if (self.get_bank_account().get_name() != another_user.get_bank_account().get_name()):
            print("Tidak bisa transfer ke user beda bank")
            return
        
        another_user.add_amount_to_balance(amount)
        