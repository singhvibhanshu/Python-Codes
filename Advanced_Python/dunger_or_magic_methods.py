class Person:
    def __init__(self, name):
        self.name = name  # Initialize the object with a name

    def __repr__(self):
        return f"Person({self.name})"  # String representation for debugging

    def __mul__(self, x):
        if type(x) is not int:  # Validate the argument to ensure it's an integer
            raise Exception("Invalid argument, must be int")
        self.name = self.name * x  # Multiply the name by an integer x

    def __call__(self, y):
        print("Call this function", y)  # Makes the object callable like a function

    def __len__(self):
        return len(self.name)  # Returns the length of the name attribute

p = Person("Vibhanshu")  # Create a new Person object with the name "Vibhanshu"
p * 5  # Calls the __mul__ method, multiplying the name by 5
print(p)  # Calls the __repr__ method, which will return the string representation of the object
print(len(p))  # Calls the __len__ method, which returns the length of the name ("Vibhanshu")

#Output:
