import collections
from collections import namedtuple

Point = namedtuple("Point", "x y z") # Point is the name of the tuple and x y z are the fields
# it automatically divides the string x y z into different segments (means it breaks into segments whenever it counter a gap/space) 
Point = namedtuple("Point", ['x', 'y', 'z']) # can also be written in lists

newP = Point(3, 4, 5)
print(newP)