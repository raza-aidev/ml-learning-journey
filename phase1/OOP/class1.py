class Dog:

    breed = "cane"
    purpose = "Gaurd Dog"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        # print(f'I am a {Dog.purpose}.')

    def bark(self):
        return f"Woof! it's {self.name} and i'm {self.age} years old. And I'm {Dog.breed} dog... Woof! Woof!"
    
    def run(self):
        return f"I'm {self.name}....weee!!! i'm running behind vehicles"

d1 = Dog('Max', '4')
d2 = Dog('Lucy', '15')

print(d1.bark())
print(d1.run())

print(d2.bark())
print(d2.run())
# d1.Dog(f"{d1.}")


"""
Inside the editor, complete the following steps:
Create a class called Person
Add an __init__ method that takes name and age as parameters
Add a method called greet that prints "Hello, my name is " followed by the name
Create an object p1 of the class with name "John" and age 36
Call the greet method on p1

"""

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and age is {self.age}")
    
p1 = Person("Jhon", 36)

p1.greet()