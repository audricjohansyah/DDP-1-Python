# class SpecialList:
#     def __init__(self, mylist):
#         self.special = mylist

#     def __str__(self):
#         return self.special

#     def __floordiv__(self, n):
#         result = [i//n if isinstance(i, int) else None for i in self.special]
#         return result

#     def __mod__(self,n):
#         result = [i%n if isinstance(i, int) else None for i in self.special]
#         return result

# a = SpecialList(["a",True,2])
# print(a.__floordiv__(1))

# def alien_lang(some_str):
#     vocal = ['a', 'i', 'u', 'e', 'o']

#     if len(some_str) == 1:
#         return f'{some_str}g{some_str}' if some_str in vocal else some_str

#     else:
#         return alien_lang(some_str[:len(some_str)//2]) + alien_lang(some_str[len(some_str)//2:])

# print(alien_lang('Nama saya Budi')) # Nagamaga sagayaga Bugudigi
# print(alien_lang('Halo')) # Hagalogo
# print(alien_lang('crwt')) # crwt
# print(alien_lang("pussy"))


# lst = [0,0,0]

# if not len(lst):
#     print("yes")

# def f_rec(s):
#     if not s:
#         return s
#     elif len(s) == 1:
#         return s
#     else:
#         if s[0] == s[-1]: return s[0] + f_rec(s[1:-1]) + s[-1]

# print(f_rec("a"))

# n = int(input("brp kali"))
# dict = {}
# for i in range (n):
#     lst = input().split()
#     a = lst[0]
#     b = lst[1]
#     dict[a] = b
#     dict[b] = a

# word = input("kata dicari:")
# if word in dict:
#     print(dict[word])

# else:
#     print("gaada")

# class User:
#     def init_(self, username, password):
#         self.__username = username
#         self.__password = password
#         self.__list_of_product =[]

#     def get_username(self):
#         return self.__username

#     def get_password(self):
#         return self.__password

#     def get_list_of_product(self):
#         return self.__list_of_product

#     def beli_product(self, product):
#         self.get_list_of_product().append(product)

#     def print_list_of_product(self):
#         for product in self.get_list_of_product():
#             print(f"{product.get_nama()} dengan jumlah {product.get_jumlah()} mempunyai total harga {product.get_total_harga()}")

# class Admin(User): # 1 poin
#     def _init_(self, username, password):
#         super().__init__(username, password)

#     def hapus_barang_user(self, user, nama_barang):
#         list_of_product = user.get_list_of_product()
#         list_of_product.remove(nama_barang)

# class Kereta(object):
#     def __init__(self, gerbong_kepala):
#         self.gerbong_kepala = gerbong_kepala

#     def total_penumpang(self):
#         return self.total_penumpang_recc(self.gerbong_kepala)

#     def total_penumpang_recc(self, gerbong):
#         if gerbong == None:
#             return 0
#         else:
#             return gerbong.num_penumpang + self.total_penumpang_recc(gerbong.next)

# class Gerbong(object):
#     def __init__(self, num_penumpang, next_gerbong):
#         self.num_penumpang = num_penumpang
#         self.next = next_gerbong


# g3 = Gerbong(1, None)
# g2 = Gerbong(5, g3)
# g1 = Gerbong(2, g2)
# g0 = Gerbong(4, g1)

# krt = Kereta(g0)

# print(krt.total_penumpang()) # 12

# def is_exist(n, lst):
#     if len(lst) == 0:
#         return False

#     elif isinstance(lst[0], int):
#         if lst[0] == n:
#             return True

#     elif isinstance(lst[0], list):
#         if is_exist(n, lst[0]):
#             return True

#     return is_exist(n, lst[1:])

# print(is_exist (7, [3,[2],[[],[]],[1,[5]]]))


# def saling_follow(lst):
#     dct = {}
#     count = 0
#     for element in lst:
#         follower = element[0]
#         followee = element[1]

#         if follower not in dct:
#             dct[follower] = [followee]
#         else:
#             dct[follower].append(followee)

#         if followee in dct:
#             if follower in dct[followee]:
#                 count += 1

#     print(count)
        

# saling_follow([('rudi', 'elmo'), ('elmo', 'hakimi'), ('elmo', 'rudi'), ('hakimi', 'elmo')])

# def jumlah_sama(n,lst):
#     sum = 0
#     for element in lst:
#             sum += int(element)
#     if  n == sum:
#         return True
#     else:
#         return False

# bag_of_words = "apple orange banana banana orange pineapple apricot"
# def puzzle(bag_of_words):
#     bag_of_words = bag_of_words.split()
#     dict_ = dict()

#     for item in bag_of_words:
#         dict_[item] = dict_.get(item, 0) +1

#     select = max(dict_.values())
#     a_list = [k for k, v in dict_.items() if v == select]
#     return sorted(a_list)[0]

# print(puzzle(bag_of_words))

# import math
# class Point:
#     def __init__(self, x , y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return "({0},{1})".format(self.x, self.y)

#     def __sub__(self, other):
#         xx = self.x - other.x
#         yy= self.y - other.y
#         return Point(xx, yy)

#     def distance(self, other):
#         varr = self - other
#         return math.sqrt(varr.x**2 + varr.y**2)

# p1= Point(0,3)
# p2 = Point(2,3)

# # print(p1-p2)
# print(p1.distance(p2))
# print(Point(1,2).distance(Point(4,-2)))

# from math import *
# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         if x1 > x2:
#             self.x1 = x2
#             self.y1 = y2
#             self.x2 = x1
#             self.y2 = y2

#         else:
#             self.x1 = x1
#             self.y1 = y1
#             self.x2 = x2
#             self.y2 = y2

#     def __str__(self):
#         return f"A line from {self.x1},{self.y1} to {self.x2},{self.y2} with the length of {self.get_length()}" 

#     def get_length(self):
#         return sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)

#     def __add__(self,line2):
#         return self.get_length() + line2.get_length()

#     def __eq__(self, line2):
#         return self.get_length() == line2.get_length()

# a1 = Line(0,0,1,1) 
# b1 = Line(2,2,3,3)
# c1 = a1+b1

# class SpecialList:
#     def __init__(self, mylist):
#         self.special = mylist

#     def __str__(self):
#         return self.special

#     def __floordiv__(self, n):
#         result = [i//n if isinstance(i, int) else None for i in self.special]
#         return result

#     def __mod__(self,n):
#         result = [i%n if isinstance(i, int) else None for i in self.special]
#         return result

# a = SpecialList(["a",True,2])
# print(a.__floordiv__(1))

# def a(x,y):
#     print("dijalankan")
#     if not(x) or not(y):
#         return x+y
#     else:
#         return a(y%x, x)

# print(a(24,16))

# a = [1,2]

# def b(x):
#     x = [3,4]
#     # print(x)
#     # return x

# b(a)
# print(a)

# class Binatang:
#     pass

# class Burung(Binatang):
#     pass

# class Elang(Burung):
#     pass

# elang1 = Elang()
# burung1 = Burung()

# print(Binatang.__bases__)
# # print(burung1)


# class Mobil:
# 	roda = 4

# 	def __init__(self, merk = None, seri = None, warna = None):
# 		self.merk = merk
# 		self.seri = seri
# 		self.warna = warna

# 	def __str__(self):
# 		return f"merk: {self.merk}, seri: {self.seri}, warna: {self.warna}"

# m1 = Mobil("Toyota", "Avanza", "hitam")
# m2 = Mobil("Honda", "Jazz", "kuning")

# #cetak class attr
# print(m1.roda)
# print(m2.roda)

# #cetak instance attribute
# print(m1)
# print(m2)

# class A:
#     a = 10
#     pass

# a1 = A()
# a2 =A()
# a3 = A()

# a1.a = 10
# A.a = 100
# a1.a = a1.a + a2.a

# print(a1.a)
# print(a2.a)
# print(a3.a)

# class Mystic:
#     def __init__(self, a, b):
#         self._a = a
#         self.__b = b

#     def process(self):
#         return self.__b % self._a if self._a < self.__b else self._a % self.__b
    
#     def geta(self):
#         return self._a
    
#     def getb(self):
#         return self.__b

# m1 = Mystic(3,4)
# print(m1.process())
# print(m1.geta())
# print(m1.getb())
# print(m1._a)
# print(m1.__b)

class Person(object):
    def __get_info(self):
        return "person"
    
    def print_person(self):
        print(self.__get_info())

class Student (Person) :
    def __get_info(self):
        return "student"
    
    def help(self):
        print(self.__get_info())

person = Person()
person.print_person()
student = Student()
student.print_person()
# student.__get_info()
# student.help()