"""
Create Square all numbers

numbers = [2, 4, 6, 8, 10]

"""
numbers = [2, 4, 6, 8, 10]
squares = list(map(lambda num: num**2, numbers))

print(squares)


"""
Question 2 - Convert to Uppercase
names = ["raza", "john", "alex", "maria"]
"""

names = ["raza", "jhon", "alex", "maria"]

def to_upper(*names):
    
    for name in names:
        return str(name.upper())
    

upper_case = list(map(to_upper, names))

print(upper_case)

"""
words = ["Python", "Java", "C++", "JavaScript"]
Question 3 - Find Length of Every Word
"""
words = ["Python", "Java", "C++", "JavaScript"]
def find_length(*words):
    for word in words:
        return len(word)

word_length = list(map(find_length, words))

print(word_length)


"""
Add 18% GST to every price.
prices = [100, 250, 500, 1000]
"""
prices = [100, 250, 500, 1000]

GST = list(map(lambda num: (num*0.18)+num, prices))

print(GST)

"""
Convert Celsius to Fahrenheit
celsius = (temps * 9/5)+32
temps = [0, 10, 20, 30, 40]

"""
temps = [0, 10, 20, 30, 40]
temps_celsius = list(map(lambda temp: (temp*9/5)+32 , temps))

print(temps_celsius)

"""

Question 18
qty = [2,4,3]

price = [100,200,50]

Calculate total price of every item.

Output

[200,800,150]

"""

qty = [2,4,3]

price = [100,200,50]

def get_sum(*prices):
    
    result = 0
    for price in prices:
        result = price[0] + price[1]
        return result

consolidated = zip(qty, price)


sum_of_prices = list(map(get_sum, consolidated))

print(sum_of_prices)


"""
Question 19
first = ["Raza","John"]

last = ["Khan","Doe"]

Output

['Raza Khan','John Doe']
"""

first = ["Raza","John"]

last = ["Khan","Doe"]

def form_names(*names):
    full_name = ""
    for name in names:
        full_name = name[0] + " " + name[1]
        return full_name

names = zip(first, last)

full_names = list(map(form_names, names))

print(full_names)

