class Book:
    def __init__(self, title, authour):
        self.title = title
        self.author = authour
        self.___is_checked_out = True

class Library(Book):
    def __init__(self, title, authour, books):
        super().__init__(title, authour)
        self.__books = []
    
    def add_book(self):
        self.__books.append(Book)
    
    def check_out_book(self, title):
        self.__books.remove(title)

    def return_book(self, title):
        pass 

    def list_available_books(self):
        return self.__books
    


library = Library
library.list_available_books()