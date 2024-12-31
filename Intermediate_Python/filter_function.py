# Function to add 7 to a number
def add7(x):
    return x + 7

# Function to check if a number is odd
def isOdd(x):
    return x % 2 != 0  # returns True if x is odd, False otherwise

# Input list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter to keep only odd numbers from the list
b = list(filter(isOdd, a))  # filter function filters based on the condition provided by isOdd

print(b)  # Output: [1, 3, 5, 7, 9]
