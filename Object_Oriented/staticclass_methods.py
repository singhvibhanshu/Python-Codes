class Dog:
    dogs = []
    x = 5 # here, x is the class variable

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod # known as decorators
    def num_dogs(cls): # here, cls stands for class
        return len(cls.dogs)
    
    @staticmethod # static methods don't need the class to be called. These are known as decorators.
    def bark(n):
        """""""bark n times"""""""
        for _ in range(n):
            print("Bark!")