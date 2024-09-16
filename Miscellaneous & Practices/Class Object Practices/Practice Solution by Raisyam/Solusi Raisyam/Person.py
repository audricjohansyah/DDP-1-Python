class Course:
  def __init__(self, name: str, sks: str):
    self.name = name
    self.sks = int(sks)
    
  def __str__(self):
    return self.name


class Person:
  def __init__(self, name: str, surname: str):
    self.name = name
    self.surname = surname

  def editInfo(self, name, surname):
    self.name = name
    self.surname = surname


class Student(Person):
  def __init__(self, name: str, surname: str):
    super().__init__(name, surname)
    self.courses = []

  def addCourse(self, course: Course):
    self.courses.append(course)


class Teacher(Person):


  def __init__(self, name: str, surname: str, courses: list[Course]):
    super().__init__(name, surname)
    self.teaching_in_courses = courses

  def addCourse(self, course: Course):
    self.teaching_in_courses.append(course)

  def teach(self):
    for course in self.teaching_in_courses:
      print(f'Guru {self.name} {self.surname} mengajar kursus {course}')

c = Course('ddp', '3')
d = Course('agama', '2')
e = Course('kombis', '4')
a = Student('budi', 'anto')
b = Teacher('rian', 'fitri', [c,d,e])

b.teach()