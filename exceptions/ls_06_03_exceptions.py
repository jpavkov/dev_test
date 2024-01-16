try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Please enter a number.")
# except ZeroDivisionError:
#     print("Age cannot be zero.")
else:
    print("No exceptions were found.")
