class Dog:
    # Class variable: This variable is shared by all instances of the class
    dogs = []  # This will store all instances of the Dog class
    x = 5  # This is a class variable with a fixed value of 5

    def __init__(self, name):
        # Instance variable: This variable is specific to each instance of the class
        self.name = name
        # Add the instance (self) to the 'dogs' list whenever a new Dog is created
        self.dogs.append(self)

    @classmethod  # This decorator indicates that the following method is a class method
    def num_dogs(cls):  # 'cls' stands for the class itself
        # Return the number of dogs created by accessing the 'dogs' list from the class
        return len(cls.dogs)

    @staticmethod  # This decorator marks the method as a static method
    def bark(n):
        """Bark n times"""
        for _ in range(n):
            print("Bark!")
