class Dog(object): # here, Dog is the parent class of Cat
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("Hey! I am", self.name, "and I am", self.age, "years old.")
    def talk(self):
        print("Bark!")

class Cat(Dog): # here, Cat is the child class of Dog
    def __init__(self, name, age, color):
        super().__init__(name, age) # constructor method or the initialize method of the class Dog
        self.color = color
    def talk(self):
        print("Meow!")

v = Cat("Vibhanshu", 21, "Brown")
v.speak()
v.talk()