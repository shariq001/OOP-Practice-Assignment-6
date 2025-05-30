# Assignment 6, Question 11
# Class Methods

class Book:
    
    total_books = 0
    
    def __init__(self, title):
        self.title = title
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        Book.total_books += 1
        
        
book1 = Book("Python OOP")
book2 = Book("Python Basics")
print(f"\n- The total number of books creater are: {Book.total_books}")