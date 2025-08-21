# Example 1: Removing duplicates automatically
nums = {1, 2, 2, 3, 4, 4}
print(nums)   # Output: {1, 2, 3, 4}

# Example 2: Creating a set from a list
letters = set(["a", "b", "a", "c", "b"])
print(letters)   # Output: {'a', 'b', 'c'}

# Example 3: Adding elements to a set
fruits = {"apple", "banana"}
fruits.add("orange")
print(fruits)   # Output: {'apple', 'banana', 'orange'}

# Example 4: Checking membership
colors = {"red", "blue", "green"}
print("red" in colors)    # Output: True (because 'red' exists in the set)
print("yellow" in colors) # Output: False (not in set)
