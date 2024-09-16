# Case 2 run program - should be no error
from AdminBank import AdminBank
from ConventionalBank import ConventionalBank
from User import User
from SyariahBank import SyariahBank


conventional_bank = ConventionalBank("Bank konven", (2.5/100))
syariah_bank = SyariahBank("Syariahku")
user_a_conven = User(10000, conventional_bank) #user_a_conven balance = 10000
user_b_conven = User(20000, conventional_bank) #user_b_conven balance = 10000
user_a_syariah = User(10000, syariah_bank) #user_a_syariah balance = 10000
user_b_syariah = User(20000, syariah_bank) #user_b_syariah balance = 20000
admin_conven = AdminBank(conventional_bank)
admin_syariah = AdminBank(syariah_bank)

user_a_conven.transfer_to(user_b_conven, 20000) #Balance tidak cukup
print(f"Balance user a conven: {user_a_conven.get_balance()}")
user_a_conven.transfer_to(user_b_conven, 10000) #user_a_conven balance = 0, user_b_conven balance = 30000
print(f"Balance user a conven: {user_a_conven.get_balance()}")
print(f"Balance user b conven: {user_b_conven.get_balance()}")

user_b_conven.transfer_to(user_a_syariah, 10000) #user_b_conven balance = 13500, user_a_syariah balance = 20000
print(f"Balance user b conven: {user_b_conven.get_balance()}")
print(f"Balance user a syariah: {user_a_syariah.get_balance()}")

user_a_syariah.transfer_to(user_a_syariah, 10000) #Cannot transfer to the same account
print(f"Balance user a syariah: {user_a_syariah.get_balance()}")

user_b_syariah.transfer_to(user_a_syariah, 20000) #user_b_syariah balance = 0, user_a_syariah balance = 40000
print(f"Balance user b syariah: {user_b_syariah.get_balance()}")
print(f"Balance user a syariah: {user_a_syariah.get_balance()}")

user_b_syariah.transfer_to(user_a_conven, 30000) #Balance tidak cukup
print(f"Balance user b syariah: {user_b_syariah.get_balance()}")

admin_conven.transfer_to(user_b_conven, 1000000000) #user_b_conven balance = 1000013500
print(f"Balance user b conven: {user_b_conven.get_balance()}")

admin_syariah.transfer_to(user_a_syariah, 100000000) #user_a_syariah balance = 1000040000
print(f"Balance user a syariah: {user_a_syariah.get_balance()}")

user_a_conven.updateBalance(1) # user_a_conven balance = 0
print(f"Balance user a conven: {user_a_conven.get_balance()}")
user_b_conven.updateBalance(1) # user_b_conven balance = 1000013500
print(f"Balance user b conven: {user_b_conven.get_balance()}")
user_a_syariah.updateBalance(1) # user_a_syariah balance = 1000040000
print(f"Balance user a syariah: {user_a_syariah.get_balance()}")
user_b_syariah.updateBalance(1) # user_b_syariah balance = 0
print(f"Balance user b syariah: {user_b_syariah.get_balance()}")

