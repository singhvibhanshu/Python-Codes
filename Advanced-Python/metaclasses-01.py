# Metaclasses are advanced concepts in Python, and are used to define how classes themselves behave.
# Simply put, metaclasses define the rules for a class.

# Regular class definition
class Test():
    pass

# Print the type of the Test class. 
# The type of a class is a metaclass, which is usually 'type' by default.
print(type(Test))  # Output: <class 'type'>
