# list
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# dictionary


def save_user(**user):
    print(user)
    print(user["name"])


save_user(id=1, name="Juan", age=22)
