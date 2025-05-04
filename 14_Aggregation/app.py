# Define the Employee class
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_employee_details(self):
        return f"{self.name} works as {self.position}."

# Define the Department class
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # List to hold Employee objects

    # Method to add employees to the department
    def add_employee(self, employee):
        self.employees.append(employee)

    # Method to display all employees in the department
    def display_employees(self):
        print(f"Employees in {self.department_name} Department:")
        for employee in self.employees:
            print(employee.get_employee_details())

# Create Employee objects
employee1 = Employee("Alice", "Software Engineer")
employee2 = Employee("Wajahat Ali Khan", "Full-Stack Developer")
employee3 = Employee("Aamna Ashraf Rajput", "Python Developer")

# Create a Department object
department = Department("Technology")

# Add employees to the department
department.add_employee(employee1)
department.add_employee(employee2)
department.add_employee(employee3)

# Display all employees in the department
department.display_employees()