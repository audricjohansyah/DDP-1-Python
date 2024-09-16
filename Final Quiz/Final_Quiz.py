class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Seller(User):
    def __init__(self, name):
        super().__init__(name)
        self.lst_mesin_cuci = [1,2,3]
        self.dict_mesin_cuci = {1:"", 2: "", 3:""}
        self.harga = 5000

    def balikin_cucian(self, cust):
        is_balikin = False
        for k, v in self.dict_mesin_cuci.items():
            if cust.get_name() in self.dict_mesin_cuci[k]:
                print(f"Cucian {cust.get_name()} dengan jumlah {self.dict_mesin_cuci[k][0]} selesai.")
                self.lst_mesin_cuci.append(k)
                self.lst_mesin_cuci.sort()
                self.dict_mesin_cuci[k] = "" 
                is_balikin = True

        if is_balikin == False:
            print(f"Maaf anda belom mencuci.")

class Customer(User):
    def __init__(self, name):
        super().__init__(name)

    def mencuci(self, kg, slr):
        if len(slr.lst_mesin_cuci) != 0:
            slr.dict_mesin_cuci[slr.lst_mesin_cuci[0]] = [kg, self.get_name()]
            slr.lst_mesin_cuci.pop(0)
            price = kg*slr.harga
            print(f"{self.get_name()} harus bayar Rp{price}")

        else:
            print("Maaf mesin cuci sudah penuh.")


a = Seller("Laundry")
z = Seller("Laundry2")
b = Customer("Elon")
c = Customer("Musk")
d = Customer("Josh")
e = Customer("Simon")

b.mencuci(10, a)
c.mencuci(17, a)
d.mencuci(10, a)
# a.balikin_cucian(c)
e.mencuci(10, a)
z.balikin_cucian(b)