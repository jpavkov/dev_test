# list(), tuple(), set(), dict()

# this is the same thing:
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)

print(point["x"])
point["x"] = 10
print(point["x"])
print(point)

point["z"] = 20

print(point)

if "a" in point:
    print(point["a"])

print(point.get("a"))

print(point.get("a", -1))

# delete an item
del point["x"]
print(point)

# iterate
for key in point:
    print(key, point[key])

for x in point.items():
    print(x)

for key, value in point.items():
    print(key, value)
