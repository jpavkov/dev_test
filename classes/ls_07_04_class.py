# instance attributes: x and y (different with each instance, or object)
# class attributes: stay the same

class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "blue"

point = Point(1, 2)
print(point.default_color)
point.draw()

point = Point(3, 4)
point.draw()
