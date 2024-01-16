# instance attributes: x and y (different with each instance, or object)
# class attributes: stay the same

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()

point2 = Point.zero()
point2.draw()
