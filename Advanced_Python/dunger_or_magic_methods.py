class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.name})"
    
    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument, must be int")
        self.name = self.name * x

    def __call__(self, y):
        print("Call this function", y)

    def __len__(self):
        return len(self.name)

p = Person("Vibhanshu")
p * 5
print(p)
print(len(p))

# these double underscore (__) methods are known as dunder/magic methods