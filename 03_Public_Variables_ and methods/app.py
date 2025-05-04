class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable
    
    def start(self):        # Public method
        print(f"{self.brand} engine started!")


my_car = Car("Toyota")
print(my_car.brand)  # Access public variable
my_car.start()       # Call public method