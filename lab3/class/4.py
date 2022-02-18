class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        return self.x, self.y
    def move(self,x,y):
        self.x += x 
        self.y += y
    def dist(self):
        return abs(self.x) - abs(self.y)
p = Point(-12,5)
print(p.show())
print(p.dist())        