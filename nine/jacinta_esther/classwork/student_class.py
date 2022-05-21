class Student:
    def __init__(self, student_name, marks):
        self.marks = marks
        self.student_name = student_name

    def set_student_name(self, student_name):
        self.student_name = student_name

    def set_student_marks(self, marks):
        self.marks = marks


Esther = Student("Jay", 90)
print(Esther.__dict__)
print(Esther.student_name, Esther.marks)
Esther.set_student_name("Jay")
Esther.set_student_marks(100)

print(Esther.student_name, Esther.marks)
print(Esther.__dict__)
