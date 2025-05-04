# Define the Book class
class Book:
    # Class variable to keep track of the total number of books
    total_books = 0

    # Constructor to initialize a book and increment book count
    def __init__(self):
        Book.increment_book_count()

    # Class method to increment the book count
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Create book instances
book1 = Book()
book2 = Book()
book3 = Book()
book4 = Book()

# Print the total number of books
print(f"Total number of books: {Book.total_books}")