#1. Cree una clase de `Circle` con:
#   1. Un atributo de `radius` (radio).
# #  2. Un método de `get_area` que retorne su área.


class Circle:
    def __init__ (self, radius):
        self.radius = radius
        

    def get_area(self):
        return 3.14 * (self.radius * self.radius)

circle_1 = Circle(5)
print(circle_1.get_area())
