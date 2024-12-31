class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)  # Opens the file with the given filename and method ('w', 'r', etc.)

    def __enter__(self):
        print("Enter")  # This method is called when entering the 'with' block
        return self.file  # This value is returned and assigned to 'f' in the 'with' statement

    def __exit__(self, type, value, traceback):
        print("Exit")  # This method is called when the block is exited, whether normally or due to an exception
        self.file.close()  # Ensures that the file is properly closed

# Using the custom context manager
with File("file.txt", 'w') as f:
    print("Middle")
    f.write("Hey!")  # Writing to the file
    raise Exception()  # Simulating an error to test if the file gets closed even if an exception occurs
