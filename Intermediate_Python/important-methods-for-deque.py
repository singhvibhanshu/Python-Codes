d = deque([1, 2, 3])
d.appendleft(0)
print(d)  # Output: deque([0, 1, 2, 3])

d = deque([1, 2, 3])
d.append(4)
print(d)  # Output: deque([1, 2, 3, 4])

d = deque([1, 2, 3])
d.popleft()
print(d)  # Output: deque([2, 3])

d = deque([1, 2, 3])
d.pop()
print(d)  # Output: deque([1, 2])

d = deque([1, 2, 3])
d.clear()
print(d)  # Output: deque([])

d = deque([1, 2])
d.extend([3, 4, 5])
print(d)  # Output: deque([1, 2, 3, 4, 5])

d = deque([1, 2, 3], maxlen=3)
d.append(4)
print(d)  # Output: deque([2, 3, 4])
