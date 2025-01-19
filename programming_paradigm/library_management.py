class Book:
    def __init__(self, title, authour):
        self.title = title
        self.author = authour
        self.___is_checked_out = True
        self._books = []
    def return_book(self):
        pass

class Library(Book):
   
    def __init__(self):
        self._books = []
    
    def add_book(self):
        self._books = []
        self._books.append(Book)
    
    def check_out_book(self, title):
        self._books = []
        self._books.remove(title)

    def return_book(self, title):
        self._books = []

    def list_available_books(self):
        self._books = []
    
