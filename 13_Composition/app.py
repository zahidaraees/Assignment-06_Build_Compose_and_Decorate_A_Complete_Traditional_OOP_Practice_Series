# Define the Engine class
class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start_engine(self):
        return f"The {self.engine_type} engine is now running."

# Define the Car class with composition
class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        return f"{self.make} {self.model}: {self.engine.start_engine()}"

# Create an Engine object
engine1 = Engine("V8")

# Create a Car object and pass the Engine object to it
car1 = Car("Ford", "Mustang", engine1)

# Call the start_car method to access the Engine's start_engine method
print(car1.start_car())