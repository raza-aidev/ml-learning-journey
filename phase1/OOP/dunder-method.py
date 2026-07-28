

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



dice = Dice(4)
# print(type(dice))
for die in dice:
    print(die)
    
