from Animal import Animal

class Panda(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.is_lazy = True
    
    def sleep(self):
        print (f"A Panda named {self.name} is sleeping...")