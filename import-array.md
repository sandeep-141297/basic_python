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

👉 Do you want me to prepare a **single code file** showing both methods (`import array` vs `from array import *`) with side-by-side examples and comments?

