# Define the Dog class
class Dog:
    # Constructor to initialize the instance variables
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Instance method to make the dog bark
    def bark(self):
         print(f"{self.name}, the {self.breed}, says: Woof! Woof!")
        
# Create an instance of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")

# Call the bark method
dog1.bark()