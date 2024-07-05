# ABC module for abstraction
from abc import ABC, abstractmethod

#class should have ABC parameter
class Shape(ABC):
    
    # only defined but implemented by subclasses
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# subclass of Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # method is redefined to fulfill the implementation of abstract method
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# shape = Shape()  # This will raise an error because Shape has abstract methods
rectangle = Rectangle(3, 4)
print(rectangle.area())       # Output: 12
print(rectangle.perimeter())  # Output: 14
