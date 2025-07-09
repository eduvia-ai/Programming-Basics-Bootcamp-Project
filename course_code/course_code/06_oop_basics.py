# البرمجة الكائنية (OOP)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"My name is {self.name} and I'm {self.age} years old.")

# استخدام الكلاس
p1 = Person("Ahmed", 22)
p1.greet()