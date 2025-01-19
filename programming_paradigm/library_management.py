class Book:
    def __init__(self, title, authour):
        self.title = title
        self.author = authour
        self.___is_checked_out = True
        self.__books = []
    def return_book(self):
        pass

class Library(Book):
   
    def __init__(self):
        self.__books = []
    
    def add_book(self):
        self.__books = []
        self.__books.append(Book)
    
    def check_out_book(self, title):
        self.__books = []
        self.__books.remove(title)

    def return_book(self, title):
        self.__books = []

    def list_available_books(self):
        self.__books = []
    
