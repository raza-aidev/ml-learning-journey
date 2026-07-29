

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        """ This method represents class object in string format"""
        return f"Title: {self.title}, Author: {self.author}, num_pages: {self.num_pages}"
    
    def __eq__(self, other):
        """ This method validate if 2 objects are equal or not"""
        if self.title == other.title and self.author == other.author:
            return True
        else:
            return False
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title

    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __sub__(self, other):
        return self.num_pages - other.num_pages
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'auther':
            return self.author
        else:
            return f"key '{key}' was not found"




book1 = Book("Harry Potter and the Philosofer stone", "J.K Rowling", 555)
book2 = Book("The Hobbit", "R.R Tokien", 456)
book3 = Book("Bad Habbits", "V.R Vishnu", 146)
# book4 = Book("The Hobbit", "R.R Tokien", 116)


# print(book1)

# print(book4 == book2) # True
# print(book1 == book2) # False

# print(book1 < book2)
# print(book1 > book2)

# print("Bad" in book1)
# print("Bad" in book2)
# print("Bad" in book3)

# print(book1 + book2)
# print(book2 - book1)

# print(book1["title"])
# print(book1["auther"])

import random

class Dice:

    def __init__(self, rolls):
        self.rolls = rolls
        self.count = 0
    
    def __iter__(self):
        """ it returns itself """
        return self
    
    def __next__(self):
        if self.count < self.rolls:
            self.count += 1
            return random.randint(1,6)
        else:
            raise StopIteration



# dice = Dice(4)
# # print(type(dice))
# for die in dice:
#     print(die)
    
# class Details:

#     def __init__(self, list_of_names):
#         self.list_of_names = list_of_names
        
    
#     def __setitem__(self, index, value):
#         if len(self.list_of_names) > index:
#             self.list_of_names[index] = value
#         else:
#            print(f"The index : {index} is out of range!")

#     def __str__(self):
#         return f"The list of string: {self.list_of_names}"
    

# d = Details(["Shariq", "Murtaza", "Ali"])

# print(d)
# d[1] = "atif"

# print(d)   


class Numbers:

    def __init__(self, num):
        self.num = num
        self.counter = 0
    
    def __setitem__(self, index, value):
        if len(self.num) > index:
            self.num[index] = value
        else:
            print(f"The Index: {index} is out of range.")
    
           
    def __str__(self):
        return f"The List of Numbers: {self.num}"

nums = Numbers([1, 2, 4, 3, 5])

# print(n)
# n[3] = 45

# print(n)


"""
Question 1: Count from 1 to N

Create a class Counter.

Requirements:

Constructor accepts n.
Iterate from 1 to n.
Stop after n.

Example:

counter = Counter(5)

for i in counter:
    print(i)

Output

1
2
3
4
5
"""

class Counter:

    def __init__(self, num):
        self.num = num
        self.current = 0

    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num == 0 or self.current >= self.num:
            raise StopIteration
        
        value = self.current
        self.current += 1
        return value
    

# for count in Counter(6):
#     print(f'{count}')

"""
Question 2: Countdown

Create a class that counts backwards.

Example

counter = Countdown(5)

Output

5
4
3
2
1
"""


class BackCount:

    def __init__(self, num):
        self.num = num
        self.counter = num 
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num == 0 or self.counter == 0:
            raise StopIteration
        
        value = self.counter
        self.counter -= 1
        return value
    
# for b in BackCount(15):
#     print(b)

"""
Question 3: Even Numbers

Create an iterator that returns even numbers from 2 to 20.

Output

2
4
6
8
10
12
14
16
18
20
"""


class EvenNum:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start 
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        while self.current <= self.end:
            if self.current % 2 == 0:
                even = self.current
                self.current += 1
                return even

            self.current += 1

            if self.current == self.end or self.start == self.end:
                raise StopIteration
        


# for e in EvenNum(2, 20):
#     print(e)

"""
Input

["Red", "Green", "Blue"]

Output

Red
Green
Blue
Red
Green
Blue
...

This iterator never stops unless the user breaks out of the loop manually.
"""

class Circular:

    def __init__(self, color):
        self.color = color
        self.current = 0
        # self.end = len(self.color)
    
    def __iter__(self):
        return self
    
    def __str__(self):
        return f"Length of {self.color} is {len(self.color)}"

    def __next__(self):
        while True:
            if self.current >= len(self.color):
                self.current = 0
                # print(f"index: {self.current}")

            curr_item = self.color[self.current]
            self.current += 1
            return curr_item

colors = Circular(["Red", "Blue", "Green"])

# print(colors)
# for c in colors:
#     print(c)


"""
Question 4: Odd Numbers

Create an iterator that returns odd numbers between two given numbers.

Example

OddNumbers(7, 19)

Output

7
9
11
13
15
17
19
"""

class OddNumbers:

    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start == self.end or self.start >= self.end:
            raise StopIteration
        
        while self.start <= self.end:

            if self.start%2 != 0:
                odd = self.start
                self.start += 1
                return odd
            self.start += 1

 

for odd in OddNumbers(7, 19):
    print(odd)
            
