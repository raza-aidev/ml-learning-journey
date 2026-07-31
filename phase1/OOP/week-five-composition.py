class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheels:
    def __init__(self, size):
        self.size = size

class Car:

    def __init__(self, model, color, power, wheel_size):
        self.color = color
        self.model = model
        self.power = Engine(power)
        self.wheel_size = [Wheels(wheel_size) for wheel in range(4)] 
    
    def display_car(self):
        return f"{self.model} of {self.color} with {self.power.horse_power}(hp) and Weel size {self.wheel_size[0].size}"

c = Car("Red", "Toyota", 550, 18)
print(c.display_car())

