# A custom generator class that generates square numbers
class Gen:
    def __init__(self, n):
        self.n = n  # the limit of the number
        self.last = 0  # starting point, begins at 0

    # The __next__() method is called when next() is used on the object
    def __next__(self):
        return self.next()  # it calls the next() method to get the next value

    # The next() method generates the next square number
    def next(self):
        if self.last == self.n:  # if we've reached the limit, raise StopIteration
            raise StopIteration()
        rv = self.last ** 2  # returns the square of the last number
        self.last += 1  # increment the value of last
        return rv

# Creating an instance of the Gen class with 10 as the limit
g = Gen(10)

# Loop to continuously call next() on the generator object until StopIteration is raised
while True:
    try:
        print(next(g))  # print the next square number
    except StopIteration:  # when the generator is exhausted, stop the loop
        break
