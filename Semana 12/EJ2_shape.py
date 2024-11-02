#Cree una clase abstracta de Shape que:
# 1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
#2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
#3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC , abstractmethod
import math

class Shape (ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass

class Circle (Shape):

    def __init__ (self, radio):
        self.radio = radio

    def calculate_perimeter(self):
        return 2 * math.pi * self.radio
    
    def calculate_area(self):
        return math.pi * (self.radio ** 2)

class Square (Shape):
    def __init__ (self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side + self.side+ self.side + self.side
    
    def calculate_area(self):
        return self.side * self.side

class Rectangle (Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return self.length + self.length + self.width + self.width
    
    def calculate_area(self):
        return self.length * self.width
    

circle = Circle(7)
print("Circle")
print(f"The perimeter of the circle is: {circle.calculate_perimeter():.2f}")
print(f"The area of the circle is: {circle.calculate_area():.2f}")

square = Square(2)
print("Square")
print(f"The perimeter of the square is: {square.calculate_perimeter():.2f}")
print(f"The area of the square is: {square.calculate_area():.2f}")

rectangle = Rectangle(2,5)
print("Rectangle")
print(f"The perimeter of the rectangle is: {rectangle.calculate_perimeter():.2f}")
print(f"The area of the rectangle is: {rectangle.calculate_area():.2f}")
