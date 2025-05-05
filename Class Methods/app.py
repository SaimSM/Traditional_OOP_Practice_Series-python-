class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

if __name__ == "__main__":
    b1 = Book("1984")
    b2 = Book("Animal Farm")
    print("Books created:", Book.total_books)
