class person(object):
    population = 50  # Class variable, shared by all instances of the class

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    @classmethod
    def getPopulation(cls):
        # This method accesses the class variable "population" and can be called on the class
        return cls.population
    
    @staticmethod
    def isAdult(age):
        # This method does not require access to the instance or class. It just checks if the person is an adult.
        return age >= 18
    
    def display(self):
        # Instance method that uses instance variables
        print(self.name, "is", self.age, "years old.")

# Creating an instance of the person class
newPerson = person("Vibhanshu", 21)

# Calling class method
print(person.getPopulation())  # Output: 50, class method can be called without creating an instance

# Calling static method
print(person.isAdult(89))  # Output: True, static method can be called without creating an instance

# Displaying the information using instance method
newPerson.display()  # Output: Vibhanshu is 21 years old.



50        # From class method getPopulation()
True      # From static method isAdult()
Vibhanshu is 21 years old.   # From instance method display()
