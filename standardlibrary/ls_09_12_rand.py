import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5, 6, 7]))
print(random.choices([1, 2, 3, 4, 5], k=3))
print("".join(random.choices("abcdefghi", k=5)))

print(string.ascii_letters)
print(string.ascii_lowercase)

print("".join(random.choices(string.ascii_letters + string.digits, k=20)))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers)
print(numbers)
