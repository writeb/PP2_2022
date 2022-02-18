class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
rec = Rectangle(3,4)
print(rec.area())