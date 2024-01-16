from sys import getsizeof

# list
values_list = [x * 2 for x in range(10000)]
# for x in values_list:
#     print(x)

# tuple (generator object)
values_tuple = (x * 2 for x in range(10000))
# for x in values_tuple:
#     print(x)

# tuple (generator object) - only good for iterating
values_tuple2 = (x * 2 for x in range(1000000))


print("values_list: ", getsizeof(values_list))
print("values_tuple: ", getsizeof(values_tuple))
print("values_tuple2: ", getsizeof(values_tuple2))
