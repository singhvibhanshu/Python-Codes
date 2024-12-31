import collections
from collections import deque  # Importing deque from collections module

# Example 1: Using appendleft() and append() to add elements
d0 = deque("VIBHANSHU")  # Creating a deque from the string 'VIBHANSHU'
d0.appendleft('6')  # Adding '6' to the left side of the deque
d0.append('9')  # Adding '9' to the right side of the deque
print(d0)  # Output: deque(['6', 'V', 'I', 'B', 'H', 'A', 'N', 'S', 'H', 'U', '9'])

# Example 2: Using pop() and popleft() to remove elements
d1 = deque("HELLO")
d1.pop()  # Removing an element from the right end ('O')
d1.popleft()  # Removing an element from the left end ('H')
print(d1)  # Output: deque(['E', 'L', 'L'])

# Example 3: Using clear() to remove all elements from the deque
d2 = deque("TIM")
d2.clear()  # Removes all elements from the deque
print(d2)  # Output: deque([])

# Example 4: Using extend() to add multiple elements at once
d3 = deque()
d3.extend('69')  # Adding '6' and '9' to the deque
d3.extend("TED")  # Adding 'T', 'E', 'D' to the deque
print(d3)  # Output: deque(['6', '9', 'T', 'E', 'D'])

# Example 5: Using maxlen to set a fixed size for the deque
d4 = deque("BARNEY", maxlen=6)  # Creating a deque with a max length of 6
print(d4)  # Output: deque(['B', 'A', 'R', 'N', 'E', 'Y'])
d4.append('6')  # Adding '6' to the right end
d4.append('9')  # Adding '9' to the right end
print(d4)  # Output: deque(['A', 'R', 'N', 'E', 'Y', '6']) 
# The deque automatically removes the leftmost element ('B') to make space for the new element
