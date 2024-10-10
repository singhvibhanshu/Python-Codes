# whenever we create a class we have to add some methods/functions to it.

class Dog(object):
    def __init__(self, name): # this __init__() needs to be in most of your class and this is something which you can called as a constructor methods
        print("This is going to implement automatically, even if we are not mentioning about it.")
        self.name = name
    def speak(self):
        print("Hey! I am", self.name)

v = Dog("Vibhanshu")
t = Dog("Tarun")
v.speak()
t.speak()

# In classes, there are something we called as attributes and methods
# Methods are anything which you create using define and they look just like functions except you have to call them using the objects
# Attributes are kind of variables that belong to a certain object. In order to create an attribute, we need to use the "self" keyword. For example, self.name, self.age, self.colour, etc.
# "self" -> is stands for the instance which you are calling like in, v = Dog(), v is the instance