items = [
    ("Product4", 10),
    ("Product2", 21),
    ("Product3", 17)
]

filtered = list(filter(lambda item: item[1] >= 11, items))
print(filtered)
