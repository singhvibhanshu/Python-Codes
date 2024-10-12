class person(object):
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population
    
    @staticmethod # static method and this is similar to class method except it can be called without using the class. It means that it doesn't take a self parameter and doesn't take a class parameter.
    def isAdult(age):
        return age >= 18
    
    def display(self):
        print(self.name, "is", self.age, "years old.")

newPerson = person("Vibhanshu", 21)
print(person.getPopulation()) # printing the class methods
print(person.isAdult(89)) # printing the static methods

# static methods are used when you don't need self and the object and it's just a good organizational way to storing a bunch of methods
# class methods are just takes the actual class and then it can access anything within the class