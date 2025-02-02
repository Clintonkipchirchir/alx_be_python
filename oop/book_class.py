class Book:
    def __init__(self, title :str, authour:str, year:int):
        self.title = title
        self.author = authour
        self.year = year
        self._is_checked_out = True

    def __del__(self):
        print(f"Deleting {self.title}")
    
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

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