from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method (no implementation)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width  # Concrete implementation


if __name__ == "__main__":
    rect = Rectangle(5, 3)
    print(f"Rectangle area: {rect.area()}") 
    
   