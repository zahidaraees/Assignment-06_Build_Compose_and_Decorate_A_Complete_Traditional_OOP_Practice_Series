'''Access Modifiers ; Public, Private, and Protected'''
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable
        self.__ssn = ssn        # Private variable


emp = Employee("John Doe", 50000, "123-45-6789")

# Accessing public variable (works)
print("Public name:", emp.name)          # Output: John Doe

# Accessing protected variable (works but convention says shouldn't)
print("Protected salary:", emp._salary)  # Output: 50000 (with warning in some IDEs)

# Accessing private variable (fails with AttributeError)
try:
    print("Private SSN:", emp.__ssn)
except AttributeError as e:
    print("Error accessing private variable:", e)  # Output: 'Employee' object has no attribute '__ssn'

# Accessing private variable through name mangling (not recommended!)
print("Mangled private access:", emp._Employee__ssn)  # Output: 123-45-6789
