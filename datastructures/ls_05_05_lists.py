letters = ["a", "b", "c"]

# add
letters.append("d")
letters.insert(0, "-")

# remove
letters.pop()  # last item
letters.pop(0)  # item at index
letters.remove("b")  # removes the first instance of b
print(letters)

letters.append(["A", "B", "C", "D"])
del letters[0:1]  # removes range of items
print(letters)

letters.clear()
print(letters)
