#1
class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2

class Square:
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 4

rectangle = Rectangle(2, 4)
print(rectangle.calculate_perimeter())

square = Square(3)
print(square.calculate_perimeter())

#2
class Square:
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, n):
        self.side += n

square = Square(100)
print(square.calculate_perimeter())
square.change_size(-50)
print(square.calculate_perimeter())


#3
class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2

class Square(Shape):
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 4

a_rectangle = Rectangle(20, 50)
a_square = Square(29)

a_rectangle.what_am_i()
a_square.what_am_i()

#4

class Horse:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
class Rider:
    def __init__(self, name):
        self.name = name

rit = Rider("Rit")
tsun = Horse("Tsun", rit)
print(tsun.owner.name)
