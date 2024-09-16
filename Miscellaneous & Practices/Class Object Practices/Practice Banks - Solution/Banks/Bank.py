class Bank:
    def __init__(self, name):
        self.name = name
        self.interest = 0

    def get_name(self):
        return self.name

    def get_interest(self):
        return self.interest