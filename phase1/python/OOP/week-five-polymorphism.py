from abc import ABC, abstractmethod

class Shape:
    
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **2
    
class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height * 0.5

class Rectangle(Shape):

    def __init__(self, length, breadth, height):
        self.breadth = breadth 
        self.length = length 
        self.height = height

    def area(self):
        return self.length * self.breadth * self.height

class Square(Shape):

    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Pizza(Circle):

    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.toppings = toppings
    

Shapes = [Circle(13), Rectangle(23, 10, 5), Square(12), Triangle(33, 64), Pizza('Pineapple', 10)]

for shape in Shapes:
    print(f"{shape.area()} cm²")
    
