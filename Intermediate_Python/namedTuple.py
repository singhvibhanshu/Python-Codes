import collections
from collections import namedtuple

# Creating a named tuple 'Point' with fields 'x', 'y', 'z'
Point = namedtuple("Point", "x y z")  # You can also use a list: ['x', 'y', 'z']

# Instantiating the named tuple with values for x, y, and z
newP = Point(3, 4, 5)

# Printing the named tuple
print(newP)

# Output: Point(x=3, y=4, z=5)

# Accessing the fields of a named tuple
print(newP.x)  # Output: 3
print(newP.y)  # Output: 4
print(newP.z)  # Output: 5

# Output: Point(x=3, y=4, z=5)
# 3
# 4
# 5 
