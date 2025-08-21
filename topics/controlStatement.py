# -------------------------
# CONTROL STATEMENTS IN PYTHON
# -------------------------

# 1) if statement
# Meaning: Runs a block of code only if the condition is True
x = 10
if x > 5:
    print("x is greater than 5")   # Runs because 10 > 5


# 2) if-else statement
# Meaning: Runs 'if block' if condition is True, otherwise runs 'else block'
age = 15
if age >= 18:
    print("You can vote")   # Not executed
else:
    print("You are too young")   # Executed because 15 < 18


# 3) if-elif-else statement
# Meaning: Used when there are multiple conditions
marks = 75
if marks >= 90:
    print("Grade A")   # Not executed
elif marks >= 60:
    print("Grade B")   # Executed because 75 >= 60
else:
    print("Grade C")   # Skipped


# 4) Nested if
# Meaning: One 'if' inside another 'if'
num = 12
if num > 0:                        # Outer condition
    if num % 2 == 0:                # Inner condition
        print("Positive Even number")   # Runs because both are True


# 5) Switch Case in Python
# Note: Python has no traditional switch-case like C/Java.
#       Instead we use dictionary or match-case (Python 3.10+).

# a) Dictionary way
def switch_example(day):
    # Dictionary works like a switch
    switcher = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday"
    }
    # .get(day, "Invalid day") means: return value if found, else "Invalid day"
    return switcher.get(day, "Invalid day")

print(switch_example(2))   # Output: Tuesday
print(switch_example(5))   # Output: Invalid day


# b) match-case (Python 3.10+)
# Works similar to switch in other languages
# You are not inside a function, so as soon as you run the file, Python executes the code line by line (top to bottom).
# Since day = 3, the match block runs automatically and prints "Wednesday".
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")   # This runs because day=3
    case _:
        print("Invalid day") # Default case


# Define a function using match-case
def day_name(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid Day"   # Default case

# Function call
print(day_name(3))   # Output: Wednesday
print(day_name(5))   # Output: Friday
print(day_name(10))  # Output: Invalid Day

