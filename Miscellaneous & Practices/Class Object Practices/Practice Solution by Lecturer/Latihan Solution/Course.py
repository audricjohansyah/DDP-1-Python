class Course:
    def __init__(self, name, sks):
        self.__name = name
        self.__sks = sks
    
    def getName(self):
        return self.__name
    
    def getSks(self):
        return self.__sks