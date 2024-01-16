numbers = [1, 2, 3]
first, second, third = numbers

first = numbers[0]
second = numbers[1]
third = numbers[2]

numbers2 = [1, 2, 3, 4, 4, 4, 4, 4, 4, 7]
first, second, *others = numbers2
print(first, others)

first, *others, last = numbers2
print(first, last)
print(others)
