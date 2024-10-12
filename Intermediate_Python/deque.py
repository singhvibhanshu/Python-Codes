import collections
from collections import deque # (deque is being pronounced as "DECK" and not "DQ")

# deque is pretty much similar to the list but the reason why we use deque is because it's faster in terms of adding elemets to the end and the beginning of the list but in some cases if we want to access the random elemet then we have to use a list over deque.

d0 = deque("VIBHANSHU")
d0.appendleft('6')
d0.append('9')
print(d0)

d1 = deque("HELLO")
d1.pop()
d1.popleft()
print(d1)

d2 = deque("TIM")
d2.clear()
print(d2)

d3 = deque()
d3.extend('69')
d3.extend("TED")
print(d3)

d4 = deque("BARNEY", maxlen = 6)
print(d4)
d4.append('6')
d4.append('9')
print(d4)