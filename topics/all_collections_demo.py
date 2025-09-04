# ==============================================
# 🔹 Python Collections + Arrays Overview
# ==============================================

# ✅ LIST
# Ordered, Mutable (can change), Allows duplicates
my_list = [10, 20, 20, 30]
print("List:", my_list)           # [10, 20, 20, 30]
my_list[0] = 99                   # Modify
print("Modified List:", my_list)  # [99, 20, 20, 30]

# -------------------------------------------------

# ✅ TUPLE
# Ordered, Immutable (cannot change), Allows duplicates
my_tuple = (1, 2, 2, 3)
print("Tuple:", my_tuple)         # (1, 2, 2, 3)
# my_tuple[0] = 99  ❌ Error (can't modify)

# -------------------------------------------------

# ✅ SET
# Unordered, Unique elements only, Mutable
my_set = {1, 2, 2, 3, 4}
print("Set:", my_set)             # {1, 2, 3, 4} → duplicates removed
my_set.add(5)
print("After Add:", my_set)       # {1, 2, 3, 4, 5}

# -------------------------------------------------

# ✅ DICTIONARY (dict)
# Key-Value pairs, Keys must be unique
my_dict = {"name": "Alice", "age": 25, "city": "Delhi"}
print("Dict:", my_dict)           # {'name': 'Alice', 'age': 25, 'city': 'Delhi'}
print("Name:", my_dict["name"])   # Access by key → Alice
my_dict["age"] = 30               # Modify value
print("Updated Dict:", my_dict)   # {'name': 'Alice', 'age': 30, 'city': 'Delhi'}

# -------------------------------------------------

# ✅ ARRAY (from array module)
# Stores only single data type (faster than list)
import array
my_array = array.array('i', [1, 2, 3, 4])   # 'i' = integer type
print("Array:", my_array)                   # array('i', [1, 2, 3, 4])
print("Array First Element:", my_array[0])  # 1
my_array.append(5)                          # Add element
print("After Append:", my_array)            # array('i', [1, 2, 3, 4, 5])

# -------------------------------------------------

# ✅ NUMPY ARRAY (external library, fast for math/data science)
# Supports multi-dimensional arrays (matrix) & vectorized operations
import numpy as np
np_array = np.array([1, 2, 3, 4, 5])   # 1D NumPy array
print("NumPy Array:", np_array)        # [1 2 3 4 5]
print("Shape:", np_array.shape)        # (5,) → 1 row, 5 elements
print("Add 10:", np_array + 10)        # [11 12 13 14 15] (vectorized addition)

# 2D NumPy Array (Matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix:\n", matrix)
print("Shape:", matrix.shape)          # (2, 3) → 2 rows, 3 cols
print("Row 1:", matrix[0])             # [1 2 3]
print("Column 2:", matrix[:, 1])       # [2 5]

# ==============================================
# ✅ Summary:
# - List  → General use, mixed data types, allows duplicates
# - Tuple → Immutable (cannot change), ordered
# - Set   → Unique values only, unordered
# - Dict  → Key-Value mapping, fast lookup
# - Array → From `array` module, fixed type, memory efficient
# - NumPy → External library, very fast, supports multi-dimension (matrix, tensor)
# ==============================================
