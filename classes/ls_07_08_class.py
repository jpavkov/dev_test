# https://rszalski.github.io/magicmethods/

# instance attributes: x and y (different with each instance, or object)
# class attributes: stay the same

class Point:
    # init is a magic method
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # str is a magic method
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.y, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)
print(point == other)
print(point > other)
print(point < other)
print(point + other)
combined = point + other
print(combined.x)
