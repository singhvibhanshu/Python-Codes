# Defining the parent class 'Vehicle'
class Vehicle():
    # Constructor method (__init__) to initialize 'price', 'color', and 'gas'
    def __init__(self, price, color, gas):
        self.price = price  # Attribute for the price of the vehicle
        self.color = color  # Attribute for the color of the vehicle
        self.gas = gas      # Attribute for the amount of gas in the vehicle

    # Method to fill the gas tank to 100
    def fillUpTank(self):
        self.gas = 100

    # Method to empty the gas tank (set gas to 0)
    def emptyTank(self):
        self.gas = 0

    # Method to return the current amount of gas left in the tank
    def gasLeft(self):
        return self.gas

# Defining the 'Car' class that inherits from the 'Vehicle' class
class Car(Vehicle):
    # Constructor method (__init__) for 'Car' class
    def __init__(self, price, color, gas, speed):
        super().__init__(price, color, gas)  # Calling the parent class constructor to initialize price, color, and gas
        self.speed = speed  # Adding a new attribute specific to cars: speed

    # Method for the car to horn
    def horn(self):
        print("Beep! Beep!")  # Car's horn sound

# Defining the 'Truck' class that inherits from the 'Vehicle' class
class Truck(Vehicle):
    # Constructor method (__init__) for 'Truck' class
    def __init__(self, price, color, gas, tires):
        super().__init__(price, color, gas)  # Calling the parent class constructor to initialize price, color, and gas
        self.tires = tires  # Adding a new attribute specific to trucks: number of tires

    # Method for the truck to horn
    def horn(self):
        print("Honk! Honk!")  # Truck's horn sound
