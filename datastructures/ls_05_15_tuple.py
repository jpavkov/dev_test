point = (1, 2)
print(type(point))
point = 1,
print(type(point))
point = 1, 2
print(type(point))
point = ()
print(type(point))
point = (1, 2) + (3, 4, 5)
print(point)
point = (1, 2, 3) * 3
print(point)
point = tuple([1, 2, 4])
print(point)
point = tuple("Hello World")
print(point)
point = (1, 2, 3)
print(point[0])
print(point[0:2])
x, y, z = point
if 10 in point:
    print("exists")
else:
    print("doesn't exist")

# tuples can't be reassigned! so, can't do:
point[0] = 12
