# Using the range() function in Python
# The range() function generates a sequence of numbers and is commonly used in loops.

# Example 1: Iterating over a range starting from 0 and ending before 8
for x in range(8):  
    # The range(8) generates numbers from 0 to 7 (8 is not included).
    print(x)  # Outputs: 0, 1, 2, 3, 4, 5, 6, 7

# Example 2: Iterating over a range with start, end, and step values
for y in range(1, 89, 1):  
    # The range(1, 89, 1) starts at 1, ends before 89, and increments by 1 each time.
    print(y)  # Outputs: 1, 2, 3, ..., 88
