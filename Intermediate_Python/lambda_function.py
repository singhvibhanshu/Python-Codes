# lambda fucntion -> anonmyous function and don't take much space in your program

def func(x):
    return x + 5

print(func(9))

func2 = lambda y: y+5 # after ':' whatever we write it just gonna return the value and also it can be used inside another function
print(func2(9))

func3 = lambda a, b, c: a + b + c # we can give any number of parameter we want to give to the lambda function
print(func3(1, 2, 3))

# now, we are using the map and lambda function at the same time

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x : x + 1, li)))