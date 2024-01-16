items = [
    ("Product4", 10),
    ("Product2", 21),
    ("Product3", 17)
]

prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]
print(prices)

filtered = list(filter(lambda item: item[1] >= 11, items))
filtered = [item for item in items if item[1] >= 11]
print(filtered)
