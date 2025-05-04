# Define the class decorator with a message template
def add_greeting(message_template):
    def decorator(cls):
        def greet(self):
            # Insert object's attribute (like self.name) into the message
            return message_template.format(name=self.name)
        cls.greet = greet
        return cls
    return decorator

# Apply the decorator with a message template
@add_greeting("Hello {name}, welcome from the Decorator!")
class Person:
    def __init__(self, name):
        self.name = name

@add_greeting("Good to see you, {name}!")
class Animal:
    def __init__(self, name):
        self.name = name

# Create objects
person = Person("Alice")
animal = Animal("Bruno")

# Call greet() method
print(person.greet()) 
print(animal.greet())  