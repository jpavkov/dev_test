numbers = [3, 31, 2, 7, 9, 12, 14, 15, 22]

# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(numbers)

items = [
    ("Product4", 10),
    ("Product2", 21),
    ("Product3", 17)
]

# items.sort()
# print(items)


# def sort_item(item):
#     return item[0]


# items.sort(key=sort_item)
# print(items)


# def sort_item_price(item):
#     return item[1]


# items.sort(key=sort_item_price)
# print(items)

# Lambda function
items.sort(key=lambda item: item[1])
print(items)

items.sort(key=lambda item: item[0], reverse=True)
print(items)
