# Demonstrating classes, methods, and attributes in Python

# Defining a class 'Dog' which inherits from the 'object' class
class Dog(object):
    
    # The __init__() method is the constructor method that is automatically called when an object is created
    def __init__(self, name):  
        # The self parameter refers to the instance of the class (the specific object you create)
        # The __init__() method is called when you create an instance of the class.
        print("This is going to implement automatically, even if we are not mentioning about it.")
        self.name = name  # Assigning the name to the instance attribute 'name'

    # Defining a method called 'speak' which the Dog objects can call
    def speak(self):  
        # The 'speak' method prints a message that includes the dog's name
        print("Hey! I am", self.name)

# Creating two instances of the Dog class
v = Dog("Vibhanshu")  # v is an instance of the Dog class
t = Dog("Tarun")      # t is another instance of the Dog class

# Calling the 'speak' method for both instances
v.speak()  # Output: "Hey! I am Vibhanshu"
t.speak()  # Output: "Hey! I am Tarun"

