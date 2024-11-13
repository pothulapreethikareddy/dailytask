from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

def perimeter(self):
        return 2 * 3.14 * self.radius

# Try to instantiate abstract class
try:
    shape = Shape()
except TypeError as e:
    print(e)  
    
# Output: Can't instantiate abstract class Shape with abstract methods area, perimeter

# Instantiate concrete subclasses
rectangle = Rectangle(4, 5)
print(f"Rectangle area: {rectangle.area()}, perimeter: {rectangle.perimeter()}")

circle = Circle(3)
print(f"Circle area: {circle.area()}, perimeter: {circle.perimeter()}")


