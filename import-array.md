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


