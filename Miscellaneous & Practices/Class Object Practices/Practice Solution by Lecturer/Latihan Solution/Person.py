class Person:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def editInfo(self, name, surname):
        self.__name = name
        self.__surname = surname
    
    def getName(self):
        return self.__name