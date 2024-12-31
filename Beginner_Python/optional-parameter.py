# Demonstrating default parameters in Python functions

# Defining a function with default parameter values
def myFunc(x=3, y=0):  
    # 'x' has a default value of 3, and 'y' has a default value of 0.
    print(x + 3)  # Adds 3 to the value of 'x' and prints the result.
    print(y + 7)  # Adds 7 to the value of 'y' and prints the result.

# Calling the function with one argument
myFunc(10)  
# The argument '10' is assigned to 'x', overriding its default value.
# The default value of 'y' (0) is used since no value is provided for it.

# Output:
# 13 (10 + 3)
# 7  (0 + 7)
