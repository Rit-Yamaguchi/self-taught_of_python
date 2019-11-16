#1, 2
class Square:
    square_list = []
    def __init__(self, s):
        self.side = s

    def print (self):
        print("{} by {} by {} by {}".format(self.side, self.side, self.side, self.side))

square = Square(5)
square.print()

#3
def compare(obj1, obj2):
    return obj1 is obj2
print(compare("a", "b"))
