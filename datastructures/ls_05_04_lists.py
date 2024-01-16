letters = ["a", "b", "c", "d"]

for letter in letters:
    print(letter)

for letter in enumerate(letters):
    print(letter)

for letter in enumerate(letters):
    print(letter[0], letter[1])

items = (0, "a")
index, item = items
print(index, item)

for index, item in enumerate(letters):
    print(index, item)
