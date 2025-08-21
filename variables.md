Let’s start **step by step** from **Point 1 → Variables**.
I’ll explain **meaning → rules → examples → small exercises** so you can practice. 🚀

---

# 🐍 Python Basics – **1. Variables**

---

## ✅ What is a Variable?

👉 A **variable** is a **name (label)** that is used to store data in memory.
It works like a **container** that holds values.

Example:

```python
x = 10       # x stores 10
y = "Hello"  # y stores text
z = 3.14     # z stores decimal
```

---

## ✅ Rules for Variables

1. Must start with a **letter or underscore `_`**.

   * ✅ `name`, `_count`
   * ❌ `1name` (not allowed)

2. Can contain **letters, numbers, underscore**.

   * ✅ `student1`, `total_marks`
   * ❌ `student-name` (hyphen not allowed)

3. Python is **case-sensitive**.

   * `Name` and `name` are different.

4. Should be **meaningful** (good practice).

   * ✅ `age = 25`
   * ❌ `a = 25`

---

## ✅ Assigning Values

👉 Python allows different ways:

```python
# Single assignment
a = 5

# Multiple variables, single value
x = y = z = 100

# Multiple variables, multiple values
name, age, city = "Aarti", 25, "Delhi"

print(name, age, city)
```

---

## ✅ Dynamic Typing

👉 Python doesn’t need type declaration.
Variable type is decided automatically.

```python
x = 10       # int
x = "Hello"  # now str
print(x)
```

---

## ✅ Variable Types (by scope)

* **Global variable** → accessible everywhere.
* **Local variable** → created inside a function, accessible only there.

```python
name = "Global Variable"

def greet():
    msg = "Local Variable"
    print(msg)   # local

greet()
print(name)      # global
```

---

## 📝 Small Exercises (Practice)

1. Create variables: `name`, `age`, `city` and print them.
2. Assign one value to multiple variables (`x = y = z = 50`). Print all.
3. Swap values of two variables without using a third variable.
   *(Hint: `a, b = b, a`)*
4. Try writing variable names with rules:

   * Which are valid? `student_name`, `2marks`, `_score`, `total%marks`

---
