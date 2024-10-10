class Vehicle():
    def __init__(self, price, color, gas):
        self.price = price
        self.color = color
        self.gas = gas
    def fillUpTank(self):
        self.gas = 100
    def emptyTank(self):
        self.gas = 0
    def gasLeft(self):
        return self.gas
    
class Car(Vehicle):
    def __init__(self, price, color, gas, speed):
        super().__init__(price, color, gas)
        self.speed = speed
    def horn(self):
        print("Beep! Beep!")

class Truck(Vehicle):
    def __init__(self, price, color, gas, tires):
        super().__init__(price, color, gas)
        self.tires = tires
    def horn(self):
        print("Honk! Honk!")