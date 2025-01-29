class Book:
    def __init__(self, title, authour):
        self.title = title
        self.author = authour
        self._is_checked_out = True
    
class Library:
   
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                return True
        return False
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                self._books.append(book)
                return True
        return False
        
    def list_available_books(self):
        for book in self._books:
            print(book.title + " by " + book.author)


  # Setup a small library
library = Library()
library.add_book(Book("Brave New World", "Aldous Huxley"))
library.add_book(Book("1984", "George Orwell"))

# Initial list of available books
print("Available books after setup:")
library.list_available_books()

# Simulate checking out a book
library.check_out_book("1984")
print("\nAvailable books after checking out '1984':")
library.list_available_books()

# Simulate returning a book
library.return_book("1984")
print("\nAvailable books after returning '1984':")
library.list_available_books()