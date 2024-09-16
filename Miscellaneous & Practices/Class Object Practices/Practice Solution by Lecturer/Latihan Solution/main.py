from Course import Course
from Student import Student
from Teacher import Teacher

course_ddp = Course("DDP-1", 4)
student_1 = Student("Asep", "Saipul")
teacher = Teacher("Rian", "F")

teacher.addCourse(course_ddp)
student_1.addCourse(course_ddp)
teacher.teach()
student_1.getCourses()