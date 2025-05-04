# Step 1: Create a custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older."):
        self.message = message
        super().__init__(self.message)

# Step 2: Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be at least 18 years old.")
    else:
        print("Age is valid. Access granted!")

# Step 3: Use try-except to handle the exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Error:", e)
except ValueError:
    print("Error: Please enter a valid number.")