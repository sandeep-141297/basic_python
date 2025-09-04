**you must import `array`** before using it in Python.

👉 Reason:

* `list`, `tuple`, `dict`, `set` are **built-in types** in Python → they don’t need import.
* But `array` comes from the **`array` module** in the Python Standard Library → so you need:

```python
import array

# Create an integer array ('i' = int type)
my_array = array.array('i', [1, 2, 3, 4])

print("Array:", my_array)              # array('i', [1, 2, 3, 4])
print("Array First Element:", my_array[0])  # 1
```

✅ Without `import array`, Python won’t recognize `array` and will throw:

```
NameError: name 'array' is not defined
```

---

* list (no import),
* tuple (no import),
* dict (no import),
* set (no import),
* array (with import array)

---

👍In Python, you can import the `array` module in **two ways**:

---

## ✅ 1. Using `import array`

* You import the whole module.
* You need to **prefix** with `array.` when creating arrays.

```python
import array  

# Create integer array ('i' means int)
arr1 = array.array('i', [1, 2, 3, 4])  

print("Array 1:", arr1)         # array('i', [1, 2, 3, 4])
print("First Element:", arr1[0])  # 1
```

👉 Here, every time you create or use an array, you must write `array.array(...)`.

---

## ✅ 2. Using `from array import *`

* This imports **all names directly** from the module.
* You can use `array(...)` **without prefix**.

```python
from array import *  

# Now we can directly use array() without "array." prefix
arr2 = array('i', [5, 6, 7, 8])  

print("Array 2:", arr2)         # array('i', [5, 6, 7, 8])
print("Second Element:", arr2[1])  # 6
```

---

## 🔹 Difference between `import array` and `from array import *`

| Import Style          | How to Use                  | Example                     |
| --------------------- | --------------------------- | --------------------------- |
| `import array`        | Must use module name prefix | `array.array('i', [1,2,3])` |
| `from array import *` | Use directly, no prefix     | `array('i', [1,2,3])`       |

---

⚠️ **Best Practice**

* Prefer `import array` → safer, avoids naming conflicts.
* `from array import *` → shorter, but not recommended in large projects because it can override names from other modules.

---

**types of values** (data types) that an `array` in Python can store.
In Python’s `array` module, every array must have **only one type of value**, and this is decided using a **type code** when creating the array.

---

## ✅ Supported Type Codes in `array` Module

| Type Code | Data Type            | Size (bytes) | Example Values                |
| --------- | -------------------- | ------------ | ----------------------------- |
| `'b'`     | Signed char (int)    | 1            | -128 to 127                   |
| `'B'`     | Unsigned char (int)  | 1            | 0 to 255                      |
| `'u'`     | Unicode character    | 2 or 4       | 'a', 'A', '😊'                |
| `'h'`     | Signed short (int)   | 2            | -32768 to 32767               |
| `'H'`     | Unsigned short (int) | 2            | 0 to 65535                    |
| `'i'`     | Signed int           | 4            | -2147483648 to 2147483647     |
| `'I'`     | Unsigned int         | 4            | 0 to 4294967295               |
| `'l'`     | Signed long          | 4            | Same as `'i'` in many systems |
| `'L'`     | Unsigned long        | 4            | Same as `'I'`                 |
| `'q'`     | Signed long long     | 8            | Very large int                |
| `'Q'`     | Unsigned long long   | 8            | Very large int                |
| `'f'`     | Float                | 4            | 1.5, 3.14                     |
| `'d'`     | Double (float)       | 8            | 2.718, 9.81                   |

---

## ✅ Example Code (All Types with Comments)

```python
from array import *

# 🔹 Integer array (signed int)
arr_int = array('i', [1, 2, 3, 4])
print("Integer Array:", arr_int)

# 🔹 Unsigned int (only positive)
arr_uint = array('I', [10, 20, 30])
print("Unsigned Int Array:", arr_uint)

# 🔹 Float array
arr_float = array('f', [1.5, 2.3, 3.9])
print("Float Array:", arr_float)

# 🔹 Double precision float
arr_double = array('d', [2.718, 3.14159])
print("Double Array:", arr_double)

# 🔹 Unicode character array
arr_char = array('u', ['a', 'b', '😊'])
print("Char Array:", arr_char)

# 🔹 Signed short
arr_short = array('h', [-300, 1000, 2000])
print("Short Int Array:", arr_short)

# 🔹 Unsigned short
arr_ushort = array('H', [100, 50000])
print("Unsigned Short Array:", arr_ushort)
```

---

## ✅ Key Points

* You must specify a **type code** when creating an array.
* All elements inside the array must match that type.
* Arrays are **more memory efficient** than lists because they fix one data type.

---

Python’s **built-in `array` module** only supports **basic numeric types** (like `int`, `float`, `double`, etc.) and **characters (`'u'` for Unicode)** — but **not full strings**.

That’s why this works ⬇️

```python
from array import array

# Integer array
arr_int = array('i', [1, 2, 3, 4])
print("Integer Array:", arr_int)

# Float array
arr_float = array('f', [1.1, 2.2, 3.3])
print("Float Array:", arr_float)

# Character array (NOT full strings, only single characters)
arr_char = array('u', ['a', 'b', 'c'])
print("Character Array:", arr_char)
```

✅ Output:

```
Integer Array: array('i', [1, 2, 3, 4])
Float Array: array('f', [1.100000023841858, 2.200000047683716, 3.299999952316284])
Character Array: array('u', 'abc')
```

❌ But this will NOT work:

```python
arr_str = array('u', ["hello", "world"])  # ❌ Error: only single characters allowed
```

---

👉 If you need to store **full strings**, then:

* Use a **list**: `["hello", "world"]`
* Or use **NumPy arrays** with `dtype='<U'` (Unicode string)

Example with NumPy:

```python
import numpy as np

np_str = np.array(["hello", "world"])
print("NumPy String Array:", np_str)
```






