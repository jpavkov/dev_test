# Class: blueprint for creating objects
# Object: instance of a class

# Human: blueprint for creating humans
# Object: John, Mary, Billy

class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, int))
