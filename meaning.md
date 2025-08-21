**meanings (definitions) + small example** for each topic so that it’s crystal clear.
Here’s a **simple glossary-style explanation** with examples.

---

# 🐍 Python Basics – Meanings + Examples

---

### **1. Variables**

👉 A variable is a **name that stores data in memory**.

```python
x = 10
y = "Hello"
print(x, y)   # 10 Hello
```

---

### **2. Data Types**

👉 The **kind of data** a variable holds.

* int → numbers (5)
* float → decimals (3.14)
* str → text ("Hello")
* bool → True/False

```python
a = 100       # int
b = 3.5       # float
c = "Hi"      # str
d = True      # bool
```

---

### **3. Built-in Types**

👉 Data types already **provided by Python** (int, str, list, dict, etc).

```python
print(type(123))    # <class 'int'>
print(type("Hi"))   # <class 'str'>
```

---

### **4. Control Statements**

👉 Used to **control program flow** (decisions).

#### if-else:

```python
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

#### elif:

```python
marks = 70
if marks > 90: print("A")
elif marks > 60: print("B")
else: print("C")
```

---

### **5. Switch (Alternative in Python)**

👉 Python doesn’t have switch-case, we use dictionary mapping.

```python
def day(num):
    return {1: "Mon", 2: "Tue"}.get(num, "Invalid")
print(day(2))   # Tue
```

---

### **6. Loops**

👉 Loops repeat code multiple times.

#### for loop:

```python
for i in range(3):
    print(i)   # 0,1,2
```

#### while loop:

```python
i = 1
while i <= 3:
    print(i)
    i += 1
```

---

### **7. Array (List in Python)**

👉 Ordered collection of values.

```python
arr = [10, 20, 30]
arr.append(40)
print(arr)   # [10, 20, 30, 40]
```

---

### **8. String**

👉 A **sequence of characters** inside quotes.

```python
s = "Python"
print(s.upper())  # PYTHON
print(s[0:3])     # Pyt
```

---

### **9. Functions**

👉 A **block of reusable code**.

```python
def greet(name):
    return "Hello " + name

print(greet("Sandeep"))
```

---

### **10. `def` Keyword**

👉 Used to **define a function**.

```python
def add(a, b):
    return a+b
print(add(2,3))
```

---

### **11. Indentation**

👉 **Spaces** used to show code blocks (instead of `{ }`).

```python
if True:
    print("Indented correctly")  # ✅
```

---

### **12. Classes & Objects**

👉 **Class** = blueprint, **Object** = instance of class.

```python
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Aarti")   # object created
print(p1.name)
```

---

### **13. Instance Object vs Class Object**

👉

* **Instance object** → created from class (unique).
* **Class object** → shared definition (blueprint).

```python
class Student:
    school = "ABC"       # class variable
    def __init__(self, name):
        self.name = name # instance variable

s1 = Student("Aarti")   # instance object
s2 = Student("Sandeep")
print(s1.name, s1.school)
```

---

### **14. `__init__()`**

👉 A **special constructor method** in class that runs automatically when object is created.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

c = Car("Toyota")
print(c.brand)
```

---

### **15. Class Member**

👉 Variables + functions **inside class**.

```python
class MyClass:
    class_var = "Shared"   # class member
    def show(self):        # method (function in class)
        print("Hello")

obj = MyClass()
obj.show()
```

---

### **16. Shell**

👉 Python **interactive console** where we type code line by line.

```bash
>>> x = 5
>>> x + 10
15
```

---

### **17. Functions in Class (Methods)**

👉 Functions written **inside class**.

```python
class Calc:
    def add(self, a, b):
        return a+b

c = Calc()
print(c.add(5, 3))
```

---

### **18. Types of Variables (Scope in Class)**

👉

* **Instance Variable** → specific to each object
* **Class Variable** → shared across all objects
* **Local Variable** → defined inside method only

```python
class Demo:
    class_var = "Shared"     # class variable
    def __init__(self, val):
        self.instance_var = val   # instance variable
    def method(self):
        local_var = "Temporary"   # local variable
        print(local_var)

d = Demo("Unique")
print(d.instance_var)
print(Demo.class_var)
d.method()
```

---

✅ Now you have **meanings + small examples** for all the basics.


