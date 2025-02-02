class Book:

    books = []
    def __init__(self, title :str, authour:str):
        self.title = title
        self.author = authour
    
    def __str__(self):
        return f"{self.__class__.__name__}{self.title} by {self.author}"

class EBook(Book):

    def __init__(self, title :str, authour:str, file_size:float):
        super().__init__(title, authour)
        self.file_size = file_size

    def __str__(self):
        return f"{self.__class__.__name__}{self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):

    def __init__(self, title :str, authour:str, page_count:float):
        super().__init__(title, authour)
        self.page_count = page_count

    def __str__(self):
        return f"{self.__class__.__name__}{self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
   
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)
    
    def list_books(self):
        for book in self._books:
            print(book)