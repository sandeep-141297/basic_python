# -------------------------
# LOOPS IN PYTHON
# -------------------------

# 1) for loop
# Meaning: Used to iterate over a sequence (list, string, range, etc.)
for i in range(5):  
    print(i)   # Prints numbers 0 to 4


# 2) for-in loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)   # Prints each fruit name one by one


# 3) for-in loop with string
for ch in "Python":
    print(ch)   # Prints each character separately


# 4) while loop
# Meaning: Runs until condition becomes False
count = 0
while count < 3:
    print("Count is:", count)   # Runs 3 times
    count += 1   # Increment count


# 5) Nested loops (loop inside another loop)
for i in range(1, 4):  
    for j in range(1, 3):
        print(f"i={i}, j={j}")   # Prints pair combinations


# 6) Loop with break
# Meaning: break stops the loop immediately
for num in range(1, 6):
    if num == 3:
        break   # Loop ends when num == 3
    print(num)   # Prints 1, 2


# 7) Loop with continue
# Meaning: continue skips the current iteration
for num in range(1, 6):
    if num == 3:
        continue   # Skips printing 3
    print(num)   # Prints 1, 2, 4, 5


# 8) pass statement
# Meaning: Does nothing (placeholder when no code yet)
for num in range(1, 4):
    pass   # Loop runs but nothing happens


# 9) for-else loop
# Meaning: else block runs only if loop finishes normally (no break)
for num in range(1, 4):
    print(num)
else:
    print("Loop completed without break")   # Runs after normal loop


# 10) while-else loop
# Meaning: else block runs only if while loop ends without break
count = 0
while count < 2:
    print("Count:", count)
    count += 1
else:
    print("While loop ended normally")   # Runs because no break
