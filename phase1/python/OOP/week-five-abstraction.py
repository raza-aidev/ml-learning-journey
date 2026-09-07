from abc import ABC , abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("Driving the car")
    
    def stop(self):
        print("Stop the car")

class Motor_Cycle(Vehicle):
    def go(self):
        print("Riding the motor cycle")
    
    def stop(self):
        print("Stop the motor cycle")

c = Car()
c.go()

b = Motor_Cycle()
b.stop()