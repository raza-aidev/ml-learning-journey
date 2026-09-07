"""  
Part 1: Inheritance (Easy)
Question 1: Vehicle Hierarchy

Create the following classes:

Vehicle
    |
    +---- Car
    |
    +---- Bike
    |
    +---- Truck
Vehicle

Attributes

brand
model
speed

Methods

start()
stop()
accelerate(speed)
brake(speed)
display_info()

Each child class should inherit from Vehicle.

Extra

Car has doors
Bike has helmet_required
Truck has load_capacity
"""
class Vehicle:

    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def start(self):
        return f"{self.model} has started."
    
    def stop(self):
        return f"{self.model} has stopped."

    def accelarate(self, speed):
        return f"{self.model} is running with the speed: {speed}km/h"
    
    def brake(self, speed):
        if speed == 0:
            return self.stop()
        else:
            return f"{self.model} has slowed down to {speed} km/h"
    
    def details_info(self):
        return print(f"It's {self.brand} {self.model} with top speed {self.speed}.")

class Car(Vehicle):
    def __init__(self, door, car_brand, model, speed):
        super().__init__(car_brand, model, speed)
        self.door = door

class Bike(Vehicle):
    
    def __init__(self, bike_brand, model, speed):
        super().__init__(bike_brand, model, speed)

    def helmet_required(self):
        return f"You must have 'Helmet' to ride a bike."

class Truck(Vehicle):

    def __init__(self,truck_brand, model, speed, load_capacity):
        super().__init__(truck_brand, model, speed)
        self.load_capacity = load_capacity

    def check_load_capacity(self):
        return f"The truck's load capacity is {self.load_capacity} Tons"


c = Car(door=4, car_brand="Toyota", speed=120, model="Vertor")
c.details_info()
print(c.brake(30))
print(c.brake(0))

print(c.stop())

t = Truck("Ashok Layland", "Everest", 200, 2000)
print(t.check_load_capacity())
