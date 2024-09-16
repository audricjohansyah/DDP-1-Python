from Person import Person

class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.__courses = []
        
    def addCourse(self, course):
        self.__courses.append(course)
    
    def getCourses(self):
        print (f"Nak {self.getName()} mengambil:")
        for course in self.__courses:
            print(f"{course.getName()} - {course.getSks()}" , end="")