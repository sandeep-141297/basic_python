# =======================================
# 🔹 PYTHON ARRAYS CHEAT SHEET (CLEAN)
# =======================================

# -----------------------------
# 1) LIST (Dynamic, Mixed Data)
# -----------------------------
# ✅ Ordered, Mutable (can change), allows duplicates
my_list_plane = [10, 20, 30, 20]
print("List:", my_list_plane)
my_list_plane[0] = 99   # ✅ change allowed
print("Modified List:", my_list_plane)

my_list = [10, 20, 30, "hello", 40.5]
print("List:", my_list)

# List Functions
my_list.append(50)         # Add element at end
my_list.insert(1, 15)      # Insert at position
my_list.remove("hello")    # Remove by value
print(my_list)
popped = my_list.pop()     # Remove last element

print("Length:", len(my_list))       # Length of list
print("Slice [0:3]:", my_list[0:3])  # Slicing
print("Search 20:", 20 in my_list)   # Search element

# -----------------------------
# 2) TUPLE (Fixed, Immutable)
# -----------------------------
# ✅ Ordered, Immutable, allows duplicates
my_tuple = (1, 2, 2, 3)
print("Tuple:", my_tuple)
# my_tuple[0] = 99  ❌ Error (can't modify)

# -----------------------------
# 3) ARRAY MODULE (Fixed Type)
# -----------------------------
# ✅ Stores only single type (lightweight like C array)
import array
my_array = array.array('i', [1, 2, 3, 4, 5])   # 'i' = int
print("Array:", my_array)

# Array Functions
my_array.append(6)             # Add element
print("Array1:", my_array)
my_array.insert(2, 10)         # Insert at index
print("Array2:", my_array)
my_array.remove(3)             # Remove by value
print("Array3:", my_array)
popped = my_array.pop()        # Remove last element
print("Array4:", my_array)
print("Index of 10:", my_array.index(10))  # Find index
print("Buffer Info:", my_array.buffer_info())  # Memory info

# -----------------------------
# 4) NUMPY ARRAY (Numerical)
# -----------------------------
# ✅ Fast, supports multi-dimension, used in Data Science
import numpy as np
np_array = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", np_array)

# NumPy Functions
# It is 1D array, so NumPy does not think in rows × columns.
# It just says → “5 elements in a single dimension” → (5,).
# That’s why you don’t see (1,5) but only (5,).
print("Shape:", np_array.shape)     # Shape of array - Means 1 row with 5 elements (1D array).

print("DType:", np_array.dtype)     # Data type
print("Size:", np_array.size)       # Number of elements
print("Slice [1:4]:", np_array[1:4])
print("Add 10:", np_array + 10)     # Vectorized operation
print("Multiply by 2:", np_array * 2)

arr = np_array.reshape(1, 5)
print("Reshaped Shape:", arr.shape)

arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("Array:\n", arr2)
print("Shape2:", arr2.shape)       # Shape - Means 2 rows with 3 elements each (2D array).
# So, .shape tells the dimensions of your array = how many rows, how many columns, how many blocks.

# -----------------------------
# 5) MULTIDIMENSIONAL ARRAY
# -----------------------------
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix Shape:", matrix.shape)   # (2,3)
print("Element [0][1]:", matrix[0][1]) # Row0 Col1
print("2nd Column:", matrix[:, 1])     # All rows, col=1
print("2nd Row:", matrix[1, :])        # All cols of row=1

# -----------------------------
# 6) JAGGED ARRAY (Unequal Rows)
# -----------------------------
# ✅ Different length rows → use dtype=object
jagged = np.array([[1, 2], [3, 4, 5], [6]], dtype=object)
print("Jagged Array:")
for arr in jagged:
    print(arr)

# -----------------------------
# 7) ARRAY ↔ STRING Conversion
# -----------------------------
# List to String
list_to_str = " ".join(map(str, my_list))
print("List → String:", list_to_str)

# Array to String
arr_to_str = " ".join(map(str, my_array))
print("Array → String:", arr_to_str)

# NumPy to String
np_to_str = np.array2string(np_array)
print("NumPy → String:", np_to_str)

# String to List
s = "10 20 30 40"
str_to_list = s.split()
print("String → List:", str_to_list)

# String to Array
str_to_array = array.array('i', map(int, s.split()))
print("String → Array:", str_to_array)


# =======================================
# ✅ SUMMARY
# =======================================
# - List       → General use, mixed data allowed
# - Tuple      → Fixed & Immutable
# - array mod  → Fixed type, memory efficient
# - NumPy arr  → Fast, numerical, supports multi-dimension
# - Matrix     → 2D/3D numerical data
# - Jagged     → Unequal row arrays
# =======================================
