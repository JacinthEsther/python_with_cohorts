class Student:

    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def __str__(self):
        return self.student_name


Esther = Student("170289", "Esther")
print(Esther.__dict__)
setattr(Esther, "student_class", 3)
print(Esther.__dict__)
delattr(Esther, "student_name")
print(Esther.__dict__)
Esther.__setattr__("student_gender", "female")
print(Esther.__dict__)
Esther.__delattr__("student_class")
print(Esther.__dict__)
# print(Esther.__reduce__())
