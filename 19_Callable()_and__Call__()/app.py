class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    # Define the __call__ method
    def __call__(self, number):
        return number * self.factor

# Create an object of Multiplier
multiply_by_3 = Multiplier(3)

# Test if the object is callable
print("Is the object callable?", callable(multiply_by_3))

# Call the object like a function
result = multiply_by_3(10)
print("Result of multiplication:", result)