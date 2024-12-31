import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()  # Start time
        rv = func(*args, **kwargs)  # Call the original function
        total = time.time() - start  # Calculate elapsed time
        print("Time:", total)  # Print the time taken
        return rv
    return wrapper

@timer
def test():
    for _ in range(100000):
        pass

@timer
def test2():
    time.sleep(2)

test()   # Will print the time taken to run the loop in test()
test2()  # Will print the time taken for 2-second sleep in test2()
