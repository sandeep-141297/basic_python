# Built-in Types

# Numbers (int, float, complex)
x = 10           # int → whole number
y = 3.14         # float → decimal number
z = 2 + 3j       # complex → number with real + imaginary part
print(x, y, z)   # Output: 10 3.14 (2+3j)

# String (str)  
name = "Python"
print(name)      # Output: Python

# List (ordered, allows duplicates, mutable)
fruits = ["apple", "banana", "apple"]
print(fruits)    # Output: ['apple', 'banana', 'apple']

# Tuple (ordered, allows duplicates, immutable)
coords = (10, 20, 30)
print(coords)    # Output: (10, 20, 30)

# Set (unordered, unique elements only)
unique_nums = {1, 2, 2, 3}
print(unique_nums)  # Output: {1, 2, 3}

# Dictionary (key-value pairs)
person = {"name": "Aarti", "age": 25}
print(person)    # Output: {'name': 'Aarti', 'age': 25}

# Boolean (True/False)
is_valid = True
print(is_valid)  # Output: True

# NoneType (represents no value / empty)
nothing = None
print(nothing)   # Output: None

# 📌 1. LIST: Ordered, Mutable (can change), Allows duplicates
# List → [ ] (Square Brackets)
my_list = [1, 2, 2, 3]
print(my_list)         # [1, 2, 2, 3]
my_list[0] = 10        # ✅ can modify
print(my_list)         # [10, 2, 2, 3]

# 📌 2. TUPLE: Ordered, Immutable (cannot change), Allows duplicates
# Tuple → ( ) (Round Brackets / Parentheses) - can't modify value
my_tuple = (1, 2, 2, 3)
print(my_tuple)        # (1, 2, 2, 3)
# my_tuple[0] = 10     ❌ Error (can't modify)

# 📌 3. SET: Unordered, Mutable, No duplicates allowed
my_set = {1, 2, 2, 3}
print(my_set)          # {1, 2, 3} (duplicates removed)
my_set.add(4)          # ✅ can add new element
print(my_set)          # {1, 2, 3, 4}

# 📌 4. DICTIONARY: Key-Value pairs, Mutable, No duplicate keys
my_dict = {"a": 1, "b": 2, "a": 3}
print(my_dict)         # {'a': 3, 'b': 2} (last 'a' kept)
my_dict["c"] = 4       # ✅ can add new key-value
print(my_dict)         # {'a': 3, 'b': 2, 'c': 4}

# List
a = [1, 2, 3]
a[0] = 100
print(a)   # [100, 2, 3]

# Tuple
b = (1, 2, 3)
b[0] = 100   # ❌ Error (tuple is immutable)

