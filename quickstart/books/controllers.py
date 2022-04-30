from datetime import datetime
from django.db.models.query import QuerySet
from quickstart.books.models import Book

class BooksController:

    def check_availability(self, book: Book) -> str:
        if not book.is_available and book.return_date is not None and book.return_date > datetime.now():
            return f"Book not available. Check again after {book.return_date}"
        if not book.is_available:
            return "Book not available" 
        return "Available"

    def list_available_books(self) -> 'QuerySet[Book]':
        return Book.objects.filter(is_available=True)