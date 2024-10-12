# problem -> when we open a file and we do a bunch of stuffs and we don't reach that file.close(). Therefore, the point is how can we make sure that we reach to that file.close() method at the end?
# we can solve it by try and finally methods

class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print("Enter")
        return self.file
    
    def __exit__(self, type, value, traceback):
        print("Exit")
        self.file.close()

with File("file.txt", 'w') as f:
    print("Middle")
    f.write("Hey!")
    raise Exception()