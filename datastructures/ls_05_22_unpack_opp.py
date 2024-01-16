numbers = [1, 2, 3]
print(numbers)
print(1, 2, 3)
print(*numbers)


values = list(range(5))
print(values)

values = list(range(5))
print(values)
values = [*range(5), "Hello"]
print(values)

first = [1, 2]
second = [3]
values = [*first, *second]
print(values)

values = [*first, "a", *second, *"Hello!"]
print(values)

first = {"x": 1}
second = {"x": 10, "y": 20}
values = {**first, **second}
print(values)

values = {**first, **second, "z": 120}
print(values)
