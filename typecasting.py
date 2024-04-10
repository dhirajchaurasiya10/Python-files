import math

# This line throws an error because you're trying to concatenate a string with an integer.
e = "50"
# print(e + 2)  # This line will cause an error

# However, you can convert the string to an integer using typecasting.
e = "50"
e = int(e)
print(e + 2)  # Output: 52
