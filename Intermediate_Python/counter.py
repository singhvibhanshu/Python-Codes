# collections and more particularly about counter which is a part of collections module
# what is the collection module?
# it's a built-in module in Python which contain different types of data types which contains some cool cool and awesome information. These are extremely useful

# Container -> it is kind of a data type or an object that are going to store multiple objects. Examples: lists, sets, dictionary, tuple [inmuttable]

# Types of Collections:
# 01: Counter
# 02: Deque
# 03: namedTuple()
# 04: orderedDictionary
# 05: defaultDictionary

import collections
from collections import Counter

c = Counter("Naman")
print(c) # jiski freq jyada woh pehle print hoga
c = Counter(['a', 'a', 'b', 'c', 'c', 'c'])
print(c)
c = Counter({'a': 1, 'b': 2})
print(c)
c = Counter(cats = 1, dogs = 2)
print(c)

# .elements(), .most_common(), 