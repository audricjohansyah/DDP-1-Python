from Person import Person

class Teacher(Person):
    def __init__(self, name, surname, courses = []):
        super().__init__(name, surname)
        self.__teaching_in_courses = courses
    def addCourse(self, course):
        self.__teaching_in_courses.append(course)
    def teach(self):
        print (f"Pak/Bu {self.getName()} mengajar:")
        for course in self.__teaching_in_courses:
            print(f"{course.getName()} - {course.getSks()}" , end="")
        print("\n")