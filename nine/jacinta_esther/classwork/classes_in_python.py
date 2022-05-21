class Human:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_gender(self, gender):
        self.gender = gender

    def set_age(self, age):
        self.age = age


dami = Human(gender= "Male",name="Dami", age=30)
print(dami.name, "is a", dami.gender, "and he is", dami.age)
