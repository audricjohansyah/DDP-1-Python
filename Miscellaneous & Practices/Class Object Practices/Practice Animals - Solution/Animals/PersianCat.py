from Cat import Cat

class PersianCat(Cat):
    def __init__(self, name, is_afraid_of_hooman):
        super().__init__(name)
        self.is_afraid_of_hooman = is_afraid_of_hooman

    def play_with_hooman(self):
        if (self.is_afraid_of_hooman):
            print (f"{self.name} will play with hooman lazily")
        else:
            print (f"{self.name} will play with hooman.. meow")