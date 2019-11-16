#1
class Apple:
    def __init__(self, c, w, p, d):
        self.color = c
        self.weight = w
        self.production = p
        self.day = d
        print("created")

#2
import math
x = math.pi
class Circle:
    def __init__(self, d):
        self.diameter = d

    def area(self):
        return self.diameter ** 2 * x


circle = Circle(2)
print(circle.area())

#3
class Triangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height / 2

triangle = Triangle(2, 4)
print(triangle.area())

#4
class Hexagon:
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 6

hexagon = Hexagon(5)
print(hexagon.calculate_perimeter())
