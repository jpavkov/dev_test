try:
    age = int(input("Age: "))
except ValueError as ex:
    print("Please enter a number.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were found.")

print("Execution continues.")
