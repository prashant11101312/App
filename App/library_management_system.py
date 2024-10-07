class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}, Year: {self.year})"

class Borrower:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} ({self.email})"

class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []

    def add_book(self, title, author, isbn, year):
        new_book = Book(title, author, isbn, year)
        self.books.append(new_book)
        print(f"Added book: {new_book}")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed book: {book}")
                return
        print("Book not found")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def add_borrower(self, name, email):
        new_borrower = Borrower(name, email)
        self.borrowers.append(new_borrower)
        print(f"Added borrower: {new_borrower}")

    def remove_borrower(self, email):
        for borrower in self.borrowers:
            if borrower.email == email:
                self.borrowers.remove(borrower)
                print(f"Removed borrower: {borrower}")
                return
        print("Borrower not found")

    def borrow_book(self, isbn, email):
        for book in self.books:
            if book.isbn == isbn and not book.borrowed:
                for borrower in self.borrowers:
                    if borrower.email == email:
                        book.borrowed = True
                        borrower.borrowed_books.append(book)
                        print(f"Borrowed book: {book} by {borrower}")
                        return
                print("Borrower not found")
                return
        print("Book not available")

    def return_book(self, isbn, email):
        for book in self.books:
            if book.isbn == isbn and book.borrowed:
                for borrower in self.borrowers:
                    if borrower.email == email:
                        book.borrowed = False
                        borrower.borrowed_books.remove(book)
                        print(f"Returned book: {book} by {borrower}")
                        return
                print("Borrower not found")
                return
        print("Book not borrowed")

    def display_books(self):
        for book in self.books:
            print(book)

    def display_borrowers(self):
        for borrower in self.borrowers:
            print(borrower)