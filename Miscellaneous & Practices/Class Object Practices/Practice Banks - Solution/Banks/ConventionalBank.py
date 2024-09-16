from Bank import Bank

class ConventionalBank(Bank):
    def __init__(self, name, interest):
        super().__init__(name)
        self.interest = interest