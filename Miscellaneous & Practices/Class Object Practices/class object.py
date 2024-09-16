# class Rectangle:
#     def __init__(self, panjang: float, lebar:float):
#         self.panjang = panjang
#         self.lebar = lebar

#     def __str__(self) -> str:
#         return f"Panjang dan lebar persegi panjang: {self.panjang}, {self.lebar}"

#     def area(self):
#         return self.panjang * self.lebar

#     def perimeter(self):
#         return (self.panjang*2) + (self.lebar*2)

#     def setpanjang(self, panjang_baru):
#         self.panjang = panjang_baru

#     def setlebar(self, lebar_baru):
#         self.lebar = lebar_baru

# pp = Rectangle(9.5, 5.9)

# print(pp.perimeter(), pp.area())

# class Parkir:
#     def __init__(self, space: int=10, price: int=1000):
#         self.space = space
#         self.price = price

#     def parked(self, cars: int, jenis: str):
#         self.space -= cars
#         self.jenis = jenis
#         if self.space > 0:
#             return f"{cars} {self.jenis} barusan parkir. Sisa tempat parkir: {self.space}"

#         else:
#             return "penuh goblok"

#     def out(self, detik: int):
#         self.space += 1
#         return (detik / 10)*self.price, self.space

# tesla = Parkir()

# print(tesla.parked(1, "Tesla"))

# class Animal(): 
#     def __init__(self, name, age): 
#         self.name = name 
#         self.age = age 

#     def eat(self): 
#         print(self.name ,"is eating...") 

# class Snake(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def crawl(self):
#         print(self.name, "is crawling...")

# class Anaconda(Snake):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def bite(self):
#         print(self.name, "is biting...")

# anaconda = Anaconda("Nicki", 12)
# anaconda.crawl()
# anaconda.eat()
# anaconda.bite()

# class Person():
#     def __init__(self, name:str, surname:str):
#         self.name = name
#         self.surname = surname
    
#     def editInfo (self, name, surname):
#         self.name = name
#         self.surname = surname

# class Course():
#     def __init__(self, name:str, sks:int):
#         self.name = name
#         self.sks = sks

#     def addcourse(self, name, sks ):
#         print(self.name, self.sks)

# class Student(Person):
#     def __init__(self, name: str, surname: str):
#         super().__init__(name, surname)


# a = Student("lebron", "james")
# a.editInfo("kyrie", "irving")

# class Animal():
#     def __init__(self) -> None:
#         pass

#     def animal(self, name: str):
#         self.name = name
#         return self.name

#     def sound(self, name:str, sound:str):
#         self.sound = sound

# class Cat(Animal):
#     def __init__(self, name: str, is_agressive: bool = False):
#         super().__init__()

#     def Cat(self, name:str):
#         self.name = name
#         return self.name

#     def speak(self):
#         return "meow"

#     def play_with_hooman(self, name:str):
#         self.name = name
#         return f"{self.name} is playing with hooman"

# class Panda(Animal):
#     def __init__(self, name:str, is_lazy: bool):
#         super().__init__()
#         self.name = name

#     def Pandas(self):
#         return self.name

#     def speak(self):
#         return "roar"
    
#     def sleep(self):
#         return f"{self.name} is sleeping"

# class PersianCat(Cat):
#     def __init__(self, name:str, is_afraid_of_hooman: bool, is_agressive: bool = False):
#         super().__init__(is_agressive)
#         self.name = name
#         self.is_afraid_of_hooman = is_afraid_of_hooman
#         self.is_aggressive = is_agressive

#     def play_with_hooman(self):
#         if self.is_afraid_of_hooman == False:
#             return f"{self.name} will play with hooman lazily"
#         else:
#             return f"{self.name} will play with hooman... meow"

# class StrayCat(Cat):
#     def __init__(self,name:str, is_naughty: bool, is_agressive: bool = True):
#         super().__init__(is_agressive) 
#         self.name = name
#         self.is_naughty = is_naughty
#         self.is_aggressive = is_agressive

#     def play_with_hooman(self):
#         if self.is_naughty == True:
#             return f"{self.name} won't play with human"

#         else:
#             if self.is_aggressive == True:
#                 return f"{self.name} play with human aggressively"

#             else:
#                 return f"{self.name} play with human passively"

class Bank():
    def __init__(self, name:str, interest:float = 0):
        self.name = name
        self.interest = interest

class ConventionalBank(Bank):
    def __init__(self, name: str, interest: float):
        super().__init__(name, interest)
        self.interest = interest
        
class SyariahBank(Bank):
    def __init__(self, name: str, interest: float):
        super().__init__(name, interest)
        self.interest = interest

class User():
    def __init__(self, balance:int, bank_account):
        self.balance = balance

    def transfer_to(self, another_user, amount:int):
        if self.balance >= amount:
            self.balance -= amount
            print("sukses")

        else:
            print("ga cukup")
    
class AdminBank(User):
    def __init__(self, bank):
        super().__init__()

b = ConventionalBank("no bunga", 0.0)
a = User(1000, b)
b = User(2000, b)

a.transfer_to(b, 50000)

