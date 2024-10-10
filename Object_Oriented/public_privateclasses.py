# In Python, there is no such thing like private or public classes. It's kinda pseudo public or pseudo private class.

class _Private: # what makes this class a private class? The underscore '_' at the very beginning makes it to behave it that.
    def __init__(self, name):
        self.name = name

class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.private = _Private(name)
    def _display(self):
        print("Hello!")
    def display(self):
        print("Hey!")