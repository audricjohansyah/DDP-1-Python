from Animal import Animal

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.is_aggressive = False

    def play_with_hooman(self):
        print ("A cat is playing with hooman")