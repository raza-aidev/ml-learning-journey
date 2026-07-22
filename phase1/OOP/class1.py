class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.age = age
        self.breed = breed
        print(f"Woof! it's {name} and i'm {age} years old. And I'm {breed} dog... Woof! Woof!")

d1 = Dog('Max', 'labrador', '4')
d2 = Dog('Lucy', 'Germen S', '15')

# d1.Dog(f"{d1.}")