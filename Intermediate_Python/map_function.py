# map function -> extremely useful tool that allow us to apply a function to a list and then create a new list with those new values

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x ** x

newList = []

for i in li:
    newList.append(func(i))

print(newList)

# operation happening from line 8 to 13 can be replaced by only one line using the map function

print(list(map(func, li))) # map function, it is, here "list" is also a keyword, not a variable

print([func(x) for x in li]) # another alternative of the map function