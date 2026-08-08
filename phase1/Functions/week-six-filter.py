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
    for word in words:
        result = ""
        if len(word)>=5:
            return word
    # print(words)
        
check_len(words)

# Max_length = list(filter(check_len, words))
Max_length = list(filter(lambda word: len(word)>5, words))

print(Max_length)


"""
numbers = [-10,20,-5,0,15,-3,8]

Return only positive numbers.

"""
numbers = [-10,20,-5,0,15,-3,8]

pos_numbers = list(filter(lambda num: num>=0, numbers))
print(pos_numbers)


"""
marks = [45,78,33,90,56,28]

Passing marks = 35
"""

marks = [45,78,33,90,56,28]
print(f"{list(filter(lambda mark:mark>35, marks))}")


"""
emails = [
    "abc@gmail.com",
    "xyz",
    "john@yahoo.com",
    "hello"
]

Return only valid emails containing '@'.
"""
emails = [
    "abc@gmail.com",
    "xyz",
    "john@yahoo.com",
    "hello"
]

def check_valid_email(*emails):
    for email in emails:
        index = email.find("@")
        if index >= 0:
            return email

print(list(filter(check_valid_email, emails)))


"""
Challenge 1

Given

numbers = range(1,51)

Return the square of all even numbers divisible by 4.
"""

numbers = range(1,51)

even_numbers = list(filter(lambda n: n%4 == 0,list(filter(lambda num: num%2 == 0, numbers))))
print(even_numbers)


"""
Challenge 2

Given

names = ["john","alex","maria","robert"]

ages = [15,20,17,25]

Return

[
("ALEX",20),
("ROBERT",25)
]
"""

names = ["john","alex","maria","robert"]

ages = [15,20,17,25]
name_age = list(zip(names, ages))

def get_mature_people(name_age):
    if name_age[1] >= 18:
        return name_age


mature_people = list(filter(get_mature_people, name_age))

print(mature_people)
