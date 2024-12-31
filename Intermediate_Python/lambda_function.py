# Syntax: lambda arguments: expression

# Regular function to add 5 to the number
def func(x):
    return x + 5

# Using the function
print(func(9))  # This will print 14, because 9 + 5 = 14

# Lambda function to add 5 to the number
func2 = lambda y: y + 5
print(func2(9))  # This will print 14, because 9 + 5 = 14

# Lambda function with multiple parameters
func3 = lambda a, b, c: a + b + c
print(func3(1, 2, 3))  # This will print 6, because 1 + 2 + 3 = 6

# Using lambda function inside map to add 1 to each element in the list
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: x + 1, li)))  # It adds 1 to every element in the list and returns a new list

# Output:
# 14
# 14
# 6
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
