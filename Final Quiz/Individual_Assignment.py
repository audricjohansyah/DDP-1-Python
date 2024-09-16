from datetime import datetime

book_collection = {"Harry Potter": 2, "Elon Musk": 3, "Star Wars": 4}

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.dict_borrowed = {}
    
    def pinjam_buku(self, book):
        dt = datetime.now()
        if book in book_collection.keys():
            if book_collection[book] != 0:
                if len(self.dict_borrowed) < 1:
                    print(f"Buku '{book}' berhasil dipinjam oleh user {self.user_id} pada {dt}")
                    self.dict_borrowed[book] = f"{dt}"
                    book_collection[book] -= 1

                else:
                    print("Maaf, Anda tidak boleh meminjam buku lagi.")

            else:
                print(f"Maaf, buku '{book}' sudah habis")

        else:
            print(f"Maaf, buku '{book}' tidak ada di koleksi.")

    def balikin_buku(self, book):
        dt = datetime.now()
        if book in book_collection.keys():
            if book_collection[book]!= 0:
                if book in self.dict_borrowed:
                    print(f"Buku {book} berhasil dikembalikan oleh user {self.user_id} pada {dt}")
                    self.dict_borrowed.pop(book)
                    book_collection[book] += 1

                else:
                    print(f"Anda tidak meminjam buku '{book}'.")

            else:
                print(f"Maaf, buku '{book}' sudah habis.")

        else:
            print(f"Maaf, buku '{book}' tidak ada di koleksi.")

class Regular(User):
    def __init__(self, user_id):
        super().__init__(user_id)

class Premium(User):
    def __init__(self, user_id):
        super().__init__(user_id)

    def pinjam_buku(self, book):
        dt = datetime.now()
        if book in book_collection.keys():
            if book_collection[book] != 0:
                print(f"Buku {book} berhasil dipinjam oleh user {self.user_id} pada {dt}")
                self.dict_borrowed[book] = f"{dt}"
                book_collection[book] -= 1

            else:
                print(f"Maaf, buku '{book}' sudah habis")

        else:
            print(f"Maaf, buku '{book}' tidak ada di koleksi.")

#test case
a = Premium(420)
a.pinjam_buku("Elon Musk")
a.pinjam_buku("Harry Potter")
a.pinjam_buku("Star Wars")
print(a.dict_borrowed)
a.pinjam_buku("Star Wars")
a.pinjam_buku("Star Wars")
a.pinjam_buku("Star Wars")
a.pinjam_buku("Star Wars") #buku sudah habis
a.balikin_buku("Harry Potter") #tidak meminjam buku ini
a.pinjam_buku("no book") #buku tidak ad di koleksi
a.balikin_buku("Elon Musk")
a.balikin_buku("Elon Musk") #tidak meminjam buku ini