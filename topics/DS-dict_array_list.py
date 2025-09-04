# ============================================================
# 🔹 Python Data Structures with Custom Key-Value Explanation
# ============================================================

# -----------------------------
# 1) LIST (array-like in Python)
# -----------------------------
# ✅ Stores ordered values
# ✅ Allows duplicates
# ❌ No custom keys, only index-based access

my_list = [10, 20, 30, 40]
print("List:", my_list)
print("List First Element:", my_list[0])  # Access by index → 10


# -----------------------------
# 2) ARRAY (using array module)
# -----------------------------
# ✅ Stores only single data type (faster, memory efficient)
# ❌ No custom keys, only index-based access

import array
my_array = array.array('i', [1, 2, 3, 4])   # 'i' means int type
print("Array:", my_array)
print("Array First Element:", my_array[0])  # Access by index → 1


# -----------------------------
# 3) DICTIONARY (dict)
# -----------------------------
# ✅ Stores key → value pairs
# ✅ Custom keys allowed (like "id", "name")
# ✅ Values can be any type (int, str, list, etc.)
# ❌ No duplicate keys allowed

student = {
    "id": 101,
    "name": "Sandeep",
    "age": 25
}

print("Dictionary:", student)
print("Student Name:", student["name"])  # Access by custom key → Sandeep
print("Student ID:", student["id"])      # Access by custom key → 101


# -----------------------------
# 4) LIST OF DICTIONARIES
# -----------------------------
# ✅ Acts like an "array of objects"
# ✅ Each item is a dictionary with custom keys
# ✅ Useful for representing table-like data (like DB records)

students = [
    {"id": 101, "name": "Sandeep", "age": 25},
    {"id": 102, "name": "Aarti", "age": 22},
    {"id": 103, "name": "Ravi", "age": 30}
]

print("List of Dictionaries:", students)
print("First Student Name:", students[0]["name"])  # → Sandeep
print("Second Student ID:", students[1]["id"])     # → 102


# -----------------------------
# 5) Why Array cannot have keys?
# -----------------------------
# array.array requires a specific type (int/float), not key-value pairs.
# Example below will cause ERROR ❌
# arr = array.array('i', {"id": 1, "value": 100})  # ❌ Not allowed


# ============================================================
# ✅ Summary:
# - List       → Values only, index-based access
# - Array      → Like list but type-specific (int, float)
# - Dictionary → Custom key-value pairs (id: name)
# - List[Dict] → Array of objects (multiple records with keys)
# ============================================================
