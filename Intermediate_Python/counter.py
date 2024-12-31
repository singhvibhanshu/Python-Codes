import collections
from collections import Counter  # Importing Counter class from the collections module

# Example 1: Counting characters in a string
c = Counter("Naman")
print(c)  # Output: Counter({'N': 2, 'a': 2, 'm': 1}) 
# Characters with higher frequency are printed first

# Example 2: Counting elements in a list
c = Counter(['a', 'a', 'b', 'c', 'c', 'c'])
print(c)  # Output: Counter({'c': 3, 'a': 2, 'b': 1}) 

# Example 3: Counting with a dictionary input
c = Counter({'a': 1, 'b': 2})
print(c)  # Output: Counter({'b': 2, 'a': 1}) 

# Example 4: Counting with keyword arguments
c = Counter(cats = 1, dogs = 2)
print(c)  # Output: Counter({'dogs': 2, 'cats': 1})

c = Counter('aabcc')
print(list(c.elements()))  # Output: ['a', 'a', 'b', 'c', 'c']

c = Counter('aabcc')
print(c.most_common())  # Output: [('a', 2), ('c', 2), ('b', 1)]
print(c.most_common(1))  # Output: [('a', 2)]  # Returns the most common element

c1 = Counter('aabcc')
c2 = Counter('abbcc')
print(c1 + c2)  # Output: Counter({'b': 4, 'c': 4, 'a': 3})  # Adding counts
print(c1 - c2)  # Output: Counter({'a': 1})  # Subtracting counts
