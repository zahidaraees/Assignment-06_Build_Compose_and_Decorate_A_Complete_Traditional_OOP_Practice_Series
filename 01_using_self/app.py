'''
1. Using self
Assignment:
Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # marks is a list of subject marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Grade: {self.calculate_grade()}")

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

# Student information
# Create instances of the Student class and display their information
student1 = Student("Hayyan", [78, 90, 78])
student1.display()

student2 = Student("Affan", [90, 96, 98])   
student2.display()
