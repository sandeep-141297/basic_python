If you want **custom key → value pairs** (like `id: name`), then in Python you don’t use a **list/array**, you use a **dictionary (`dict`)**.

---

## 🔹 Example 1: Dictionary with custom keys

```python
# Dictionary (custom key-value storage)
student = {
    "id": 101,
    "name": "Sandeep",
    "age": 25
}

print(student["name"])   # Access by key → Sandeep
print(student["id"])     # Access by key → 101
```

✅ Keys are custom (`id`, `name`, `age`).
✅ Values can be anything (int, string, list, etc.).
❌ No duplicate keys allowed.

---

## 🔹 Example 2: List of Dictionaries

```python
# List of multiple students (array of dicts)
students = [
    {"id": 101, "name": "Sandeep", "age": 25},
    {"id": 102, "name": "Aarti", "age": 22},
    {"id": 103, "name": "Ravi", "age": 30}
]

print(students[0]["name"])   # First student's name → Sandeep
print(students[1]["id"])     # Second student's id → 102
```

✅ Used when you want an **array-like structure but with key-value pairs** inside.

---

## 🔹 Example 3: Using `dict` inside `array.array` ❌ (Not possible)

```python
import array

# This will throw error because array.array needs same datatype
# arr = array.array('i', {"id": 1, "value": 100})  ❌ Not allowed
```

👉 `array.array` only supports **primitive types** (int, float, etc.), not key-value pairs.

---

# ✅ Conclusion

* **List/Array** → Just values `[1, 2, 3]` (no keys).
* **Dict** → Custom `key: value` pairs.
* **List of Dicts** → Best when you want an **array of objects** like in databases.

---


