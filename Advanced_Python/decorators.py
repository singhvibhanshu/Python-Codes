import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print("Time: ", total)
        return rv
    return wrapper

@timer
def test():
    for _ in range(100000):
        pass

@timer
def test2():
    time.sleep(2)

test()
test2()