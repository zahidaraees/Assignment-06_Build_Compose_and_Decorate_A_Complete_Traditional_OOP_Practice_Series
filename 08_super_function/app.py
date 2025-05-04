'''The Super () Function'''
class Person:
    def __init__(self, name):
        self.name = name  # Set name through base class constructor

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call parent constructor using super()
        self.subject = subject  # Add subclass-specific property


if __name__ == "__main__":
    math_teacher = Teacher("Aamna Ashraf Rajput", "Mathematics")
    
    print(f"Teacher Name: {math_teacher.name}")  
    print(f"Subject: {math_teacher.subject}")       