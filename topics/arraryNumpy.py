# ================================
# 📌 What is NumPy?
# ================================
# NumPy (Numerical Python) is a powerful library in Python
# used for numerical computations, data analysis, and scientific computing.
# It provides support for:
#   - Arrays (much faster than Python lists)
#   - Mathematical operations (linear algebra, statistics, etc.)
#   - Multi-dimensional data
#   - Efficient memory usage
#   - Widely used in Data Science, Machine Learning, AI, etc.

# To install NumPy (only once in system):
# pip install numpy

import numpy as np

# ================================
# 📌 NumPy Array vs Python List
# ================================
py_list = [1, 2, 3, 4, 5]       # Python List
np_array = np.array([1, 2, 3, 4, 5])  # NumPy Array

print("Python List:", py_list)
print("NumPy Array:", np_array)

# ================================
# 📌 1D Array Example
# ================================
arr1 = np.array([10, 20, 30, 40])
print("1D Array:", arr1)

# ================================
# 📌 2D Array Example (Matrix)
# ================================
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# ================================
# 📌 3D Array Example
# ================================
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", arr3)

# ================================
# 📌 Array Functions
# ================================
print("Array Shape:", arr2.shape)      # (rows, cols)
print("Array Size:", arr2.size)        # total elements
print("Array Type:", arr2.dtype)       # data type (int32, float64, etc.)

# ================================
# 📌 Array Operations
# ================================
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])

print("Addition:", arr_a + arr_b)     # [5 7 9]
print("Subtraction:", arr_a - arr_b)  # [-3 -3 -3]
print("Multiplication:", arr_a * arr_b)  # [4 10 18]
print("Division:", arr_b / arr_a)     # [4. 2.5 2.]

# ================================
# 📌 Useful NumPy Functions
# ================================
print("Zeros Array:", np.zeros((2,3)))   # 2x3 matrix with all 0
print("Ones Array:", np.ones((2,3)))     # 2x3 matrix with all 1
print("Range Array:", np.arange(0,10,2)) # [0 2 4 6 8]
print("Linspace:", np.linspace(0,1,5))   # 5 numbers between 0 and 1

# ================================
# 📌 Statistical Functions
# ================================
nums = np.array([10, 20, 30, 40, 50])
print("Mean:", np.mean(nums))       # Average
print("Max:", np.max(nums))         # Maximum value
print("Min:", np.min(nums))         # Minimum value
print("Sum:", np.sum(nums))         # Total sum
print("Standard Deviation:", np.std(nums)) # Spread of data

# ================================
# 📌 Reshaping Arrays
# ================================
arr = np.arange(1, 10)  # [1 2 3 4 5 6 7 8 9]
print("Original Array:", arr)
reshaped = arr.reshape(3,3)   # Convert to 3x3 matrix
print("Reshaped 3x3:\n", reshaped)
