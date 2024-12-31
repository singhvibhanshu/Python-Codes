# Defining a parent class 'Dog'
class Dog(object):
    # Constructor method (__init__) to initialize attributes 'name' and 'age'
    def __init__(self, name, age):
        self.name = name  # Instance attribute 'name'
        self.age = age    # Instance attribute 'age'

    # Method to make the dog speak
    def speak(self):
        print("Hey! I am", self.name, "and I am", self.age, "years old.")
    
    # Method to simulate the dog talking
    def talk(self):
        print("Bark!")

# Defining a child class 'Cat' which inherits from 'Dog'
class Cat(Dog):
    # Constructor method (__init__) for the 'Cat' class
    def __init__(self, name, age, color):
        # Calling the parent class's constructor to initialize 'name' and 'age'
        super().__init__(name, age)
        self.color = color  # Adding a new attribute 'color' for cats

    # Overriding the 'talk' method to make the cat talk differently
    def talk(self):
        print("Meow!")

# Creating an instance of the 'Cat' class
v = Cat("Vibhanshu", 21, "Brown")

# Calling the 'speak' method (inherited from the 'Dog' class)
v.speak()  

# Calling the 'talk' method (overridden in the 'Cat' class)
v.talk()
