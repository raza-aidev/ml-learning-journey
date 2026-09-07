class Library:
    def __init__(self, lib_name):
        self.lib_name = lib_name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_of_books(self):
        return [f"{book.book_name} and {book.author}" for book in self.books] # here we are accessing list of books represented as "self.books", the list of books contains book objects containing author and name properties of books objects pass to the library.

class Books:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
    
lib = Library("Deccan Library")

book1 = Books("Harry Potter", "J.K Rowling")
book2 = Books("White House in the dark woods", "A.R Kafil")
book3 = Books("Lake of Pearls", "R.Rajkumar")

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

# print(list(lib.list_of_books()))

for book in lib.list_of_books():
    print(book)
