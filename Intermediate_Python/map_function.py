# Initial list
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Defining a function that takes a number and raises it to the power of itself
def func(x):
    return x ** x

# Using a for loop to apply the function to the list
newList = []
for i in li:
    newList.append(func(i))  # Adding the result of func(i) to the new list

# Printing the new list with modified values
print(newList)

# Using map function to achieve the same result
print(list(map(func, li)))  # map(func, li) applies func to every element of li and returns an iterator, list() converts it to a list

# Using list comprehension as an alternative to map
print([func(x) for x in li])  # Equivalent to map but written as a list comprehension
