def greet(name):
    print(f"Hi {name}")


greet("JP")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("JP")
print(message)
file = open("content.txt", "w")
file.write(message)
