# Base class Book
class Book:
    def __init__(self, title, author):
        self.title = title  # Book title
        self.author = author  # Book author
        self.is_borrowed = False  # Indicates if the book is borrowed

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True  # Mark the book as borrowed if it's not already
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is already borrowed.")  # Print a message if the book is already borrowed

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False  # Mark the book as returned if it was borrowed
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} wasn't borrowed.")  # Print a message if the book wasn't borrowed

# Magazine class (inherits from Book)
class Magazine(Book):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)  # Call the constructor of Book
        self.issue_number = issue_number  # Magazine issue number

    def borrow(self):
        print(f"{self.title}, issue {self.issue_number}, has been borrowed.")  # Overriding the borrow method for magazines

# AuthorBook class (inherits from Book)
class AuthorBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)  # Call the constructor of Book
        self.pages = pages  # Number of pages in the book

    def borrow(self):
        print(f"{self.title} by {self.author} has {self.pages} pages and has been borrowed.")  # Overriding the borrow method for author books

# Library class
class Library:
    def __init__(self):
        self.books = []  # List of books in the library

    def add_book(self, book):
        self.books.append(book)  # Add a book to the library

    def list_books(self):
        print("Books in the library:")
        for book in self.books:
            print(f"- {book.title} by {book.author}")  # Print book titles and authors

# Create book objects
book1 = AuthorBook("The Great Gatsby", "F. Scott Fitzgerald", 218)
book2 = Magazine("National Geographic", "Various", 101)
book3 = AuthorBook("1984", "George Orwell", 328)

# Create a library object
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Print the list of books in the library
library.list_books()

# Borrow books
book1.borrow()  # Author book
book2.borrow()  # Magazine
book3.borrow()  # Author book

# Return books
book1.return_book()
book2.return_book()
book3.return_book()
