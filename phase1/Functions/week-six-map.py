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
Keep only even numbers.
numbers = [5,8,12,17,19,20,25]
Question 6 - Even Numbers
"""
numbers = [5,8,12,17,19,20,25]

def is_even(*nums):
    for num in nums:
        if num%2 == 0:
            return num
    
even_nums = list(filter(is_even, numbers))

print(even_nums)

"""
Return only words having more than 5 letters.
words = ["cat","elephant","dog","python","sun"]

"""
words = ["cat","elephant","dog","python","sun"]

def check_len(*words):
    # for word in words:
    #     result = ""
    #     if len(word)>=5:
    #         return word
    # print(words)
        
check_len(words)

Max_length = list(map(check_len , words))
# print(Max_length)