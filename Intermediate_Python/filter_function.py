# filter function is very similar to map function

def add7(x):
    return x + 7

def isOdd(x):
    return x%2 != 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list(filter(isOdd, a)) # here again, "list" is a keyword and filter function is taking the two arguments. First is the function (isOdd in this case) and a list (a in this case).

print(b)