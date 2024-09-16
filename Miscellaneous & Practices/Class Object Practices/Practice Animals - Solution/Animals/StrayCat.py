from Cat import Cat

class StrayCat(Cat):
    def __init__(self, name, is_naughty):
        super().__init__(name)
        self.is_naughty = is_naughty
        self.is_aggressive = True

    def play_with_hooman(self):
        if (self.is_naughty):
            print (f"{self.name} won't play with hooman")
        else:
            if (self.is_aggressive):
                print (f"{self.name} play with hooman aggressively")
            else:
                print (f"{self.name} play with hooman passively")