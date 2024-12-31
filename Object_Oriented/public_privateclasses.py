# In Python, there are no strict access modifiers like 'private' or 'public'.
# However, Python uses conventions to indicate whether something is intended to be private or public.

# Private class - Conventionally indicated with an underscore at the beginning of the class name
class _Private:
    def __init__(self, name):
        self.name = name  # This is an attribute to store the name for the _Private class

# Public class - No underscore before the class name
class NotPrivate:
    def __init__(self, name):
        self.name = name  # This is an attribute to store the name for the NotPrivate class
        self.private = _Private(name)  # Creating an instance of the _Private class

    # Private method - Conventionally indicated with an underscore
    def _display(self):  
        print("Hello!")  # This is a private method and shouldn't be accessed directly (by convention)

    # Public method
    def display(self):  
        print("Hey!")  # This is a public method and can be accessed normally
