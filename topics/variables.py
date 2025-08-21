# Single variable assignment
x = 10        # x stores an integer value 10
print(x)     # prints 10

# String variable
name = "Aarti"   # name stores text value "Aarti"
print(name)      # prints Aarti

# Float variable
pi = 3.14     # pi stores decimal value
print(pi)    # prints 3.14

# Boolean variable
is_active = True   # is_active stores True/False
print(is_active)   # prints True

# Multiple variables, single value
a = b = c = 100    # all three variables store same value 100
print(a, b, c)     # prints 100 100 100

# Multiple variables, multiple values
name, age, city = "Sandeep", 28, "Delhi"   # each variable gets separate value

# Case-sensitive
Name = "Capital N"    # different from 'name'
name = "Small n"      
print(Name, name)     # prints both values

# Dynamic typing
var = 5           # var is integer
var = "Hello"     # now var becomes string
print(var)        # prints "Hello"

# Swap variables
a, b = 10, 20     # assign values
a, b = b, a       # swap values
print(a, b)       # prints 20 10

# Global and Local variable
msg = "Global"    # global variable
def show():
    msg = "Local" # local variable inside function
    print(msg)    # prints Local
show()
print(msg)        # prints Global
