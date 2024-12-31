# Define a metaclass named Meta
class Meta(type):
    def __new__(cls, class_name, bases, attrs):
        # Create a new dictionary to store class attributes
        a = {}
        
        # Loop through the attributes of the class
        for name, val in attrs.items():
            # If the attribute name starts with an underscore, add it unchanged
            if name.startswith("_"):
                a[name] = val
            else:
                # Otherwise, convert the attribute name to uppercase before adding it
                a[name.upper()] = val

        # Create the new class using the modified attributes
        return type(class_name, bases, a)

# Define the Dog class, using the Meta metaclass
class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("hi")

# Create an instance of Dog
d = Dog()

# Test the hello() method
print(d.hello())  # Output: hi

# Access the attributes of Dog and observe their names are now uppercased
print(d.X)  # Output: 5
print(d.Y)  # Output: 8
