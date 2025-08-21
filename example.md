Perfect! 🚀 Let’s go through **all the Python basics** you listed with **easy explanations + examples**.
(Think of this as your Python cheat sheet 📘 for fundamentals.)

---

# 🐍 Python Basics with Examples

---

## 1. **Variables**

👉 Variables are containers to store data.

```python
x = 10        # integer
y = "Hello"   # string
z = 3.14      # float

print(x, y, z)
```

---

## 2. **Data Types**

👉 Python is **dynamically typed**, meaning you don’t need to declare types.

* int → whole numbers
* float → decimal
* str → text
* bool → True/False
* list → ordered, changeable
* tuple → ordered, unchangeable
* set → unordered, unique values
* dict → key-value pairs

```python
a = 100                 # int
b = 3.5                 # float
c = "Python"            # string
d = True                # boolean
e = [1, 2, 3]           # list
f = (1, 2, 3)           # tuple
g = {1, 2, 3}           # set
h = {"name": "Aarti"}   # dictionary

print(type(f), type(h))
```

---

## 3. **Control Statements**

### (a) **if-else**

```python
age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

### (b) **Elif**

```python
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
```

---

## 4. **Switch Case (Python doesn’t have switch, use dict)**

```python
def switch_case(day):
    return {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday"
    }.get(day, "Invalid")

print(switch_case(2))   # Tuesday
```

---

## 5. **Loops**

### (a) For Loop

```python
for i in range(5):
    print(i)   # 0 to 4
```

### (b) While Loop

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

### (c) Loop with break/continue

```python
for i in range(1, 6):
    if i == 3:
        continue  # skip 3
    if i == 5:
        break     # stop loop
    print(i)
```

---

## 6. **Array (Actually List in Python)**

```python
arr = [10, 20, 30, 40]
print(arr[0])       # 10
arr.append(50)      # add element
arr.remove(20)      # remove element
print(arr)
```

---

## 7. **String**

```python
s = "Python"
print(s[0])         # P
print(s.upper())    # PYTHON
print(s.lower())    # python
print(s[0:3])       # Pyt
```

---

## 8. **Functions**

👉 Define using `def`.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Sandeep"))
```

---

## 9. **Indentation**

👉 Python uses **indentation (spaces/tabs)** instead of `{}`.

```python
if True:
    print("This is indented correctly")  # required indentation
```

❌ If wrong:

```python
if True:
print("Error!")   # ❌ IndentationError
```

---

## 10. **Classes & Objects**

```python
class Person:
    def __init__(self, name, age):   # constructor
        self.name = name             # instance variable
        self.age = age

    def greet(self):                 # method
        print(f"Hi, I'm {self.name}, {self.age} years old.")

# Creating object (instance)
p1 = Person("Aarti", 25)
p1.greet()
```

---

## 11. **Instance Object vs Class Object**

* **Instance variables** → unique to each object
* **Class variables** → shared among all objects

```python
class Student:
    school = "XYZ School"     # class variable (shared)

    def __init__(self, name):
        self.name = name      # instance variable (unique)

s1 = Student("Aarti")
s2 = Student("Sandeep")

print(s1.name, s1.school)   # Aarti XYZ School
print(s2.name, s2.school)   # Sandeep XYZ School
```

---

## 12. **`__init__()`**

👉 Special method (constructor) that runs when object is created.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

c1 = Car("Toyota", "Innova")
print(c1.brand, c1.model)
```

---

## 13. **Class Members (Methods & Variables)**

```python
class MyClass:
    class_var = "I am class variable"   # class variable

    def __init__(self, value):
        self.instance_var = value       # instance variable

    def show(self):
        print("Instance:", self.instance_var)
        print("Class:", MyClass.class_var)

obj = MyClass("Hello")
obj.show()
```

---

## 14. **Python Shell (Interactive Mode)**

👉 Run code line by line.

```bash
python
>>> x = 5
>>> x + 10
15
```

---

## 15. **Functions in Class**

👉 Methods inside class are just functions with `self`.

```python
class Calculator:
    def add(self, a, b):
        return a + b

c = Calculator()
print(c.add(5, 3))   # 8
```

---

## 16. **Types of Variables in Class (Scope Basis)**

1. **Instance Variables** → Defined in `__init__`, unique to object
2. **Class Variables** → Defined inside class, shared
3. **Local Variables** → Defined inside method, temporary

```python
class Demo:
    class_var = "Class Variable"

    def __init__(self, value):
        self.instance_var = value   # instance variable

    def method(self):
        local_var = "Local Variable"
        print(local_var)

d = Demo("Instance Value")
print(d.instance_var)   # instance
print(Demo.class_var)   # class
d.method()              # local
```

---

✅ Now you have a **complete basics roadmap with examples** 🎯
