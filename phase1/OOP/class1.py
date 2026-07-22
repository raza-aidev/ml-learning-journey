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


"""
Inside the editor, complete the following steps:
Create a class called Dog
Add an __init__ method with parameters name and age, and store them as properties using self
Add a method called bark that prints the dog's name followed by " says Woof!"
Create an object d1 of the Dog class with name "Buddy" and age 3
Call the bark method on d1
 
"""

class Dog:
    def __init__(self, name, age=6):
        self.age = age
        self.name = name
    
    def bark(self):
        print(f"{self.name} says woof!, {self.name} is {self.age}")

d1 = Dog("Buggy", 3)
d2 = Dog("Lucy")
d1.bark()
d2.bark()


""" 
we can also name self with other name, but the condition is it whoulc be the 1st parameter in the function
also Oython recommend that we should use self only.

Lets see some examples below

"""

class Guests:
    
    hotel_name = "Sharaton";
    
    def __init__(myObject, name):
        myObject.name = name

    def greeting(abc):
        return f"Welcome to the {abc.hotel_name}, Mr/Mrs.{abc.name}!"
    
    def welcome(self):
        message = self.greeting()
        print(message)

g1 = Guests("Aatir")

g1.welcome()



"""
Inside the editor, complete the following steps:
Create a class Student with an __init__ that takes name and grade, and stores them as properties
Create an object s1 with name "Anna" and grade "A"
Print the grade of s1
Change the grade of s1 to "B"
Print the updated grade
"""

class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
s1 = Student("Ana", "A")

print(f"{s1.name}'s Grade: {s1.grade}")

s1.grade = "B"
#Changing the property of the class
print(f"{s1.name}'s Grade: {s1.grade}")



