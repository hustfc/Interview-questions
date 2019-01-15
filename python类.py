class Point:
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y
p = Point(10, 10)
print(type(p))
print(p.x, p.y)
print(dir(Point))
print(help(Point))
