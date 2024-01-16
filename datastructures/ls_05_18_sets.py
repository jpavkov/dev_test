numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)

# add, remove, length
first = set(numbers)
print(first)

second = {1, 6}
second.add(5)
second.remove(5)
len(second)

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

if 1 in first:
    print("yes")
