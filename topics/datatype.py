# Integer (whole number)
num = 10          # int type → stores whole numbers
print(type(num))  # <class 'int'>

# Float (decimal number)
pi = 3.14         # float type → stores decimal values
print(type(pi))   # <class 'float'>

# String (text)
name = "Python"   # str type → stores sequence of characters
print(type(name)) # <class 'str'>

# Boolean (True/False)
is_active = True  # bool type → stores logical values
print(type(is_active))  # <class 'bool'>

# List (ordered, changeable, allows duplicates)
fruits = ["apple", "banana", "cherry"]  # list type
fruits.append("mango")                  # add new item
print(fruits)                           # ['apple','banana','cherry','mango']

# Tuple (ordered, unchangeable, allows duplicates)
numbers = (1, 2, 3, 2)   # tuple type → immutable
print(numbers)           # (1, 2, 3, 2)

# Set (unordered, unique values, no duplicates)
unique_nums = {1, 2, 2, 3}  # set type → removes duplicates automatically
print(unique_nums)          # {1, 2, 3}

# Dictionary (key-value pairs, unordered)
person = {"name": "Aarti", "age": 25, "city": "Delhi"}  # dict type
print(person["name"])   # Access value by key → Aarti

# NoneType (represents no value / empty)
x = None           # None type → used as placeholder
print(type(x))     # <class 'NoneType'>
