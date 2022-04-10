from datetime import datetime

from attr import dataclass
from quickstart.books.models import Book

class BookController:

    def check_availability(self, book: Book) -> str:
        if not book.is_available and book.return_date is not None and book.return_date > datetime.now():
            return f"Book not available. Check again after {book.return_date}"
        if not book.is_available:
            return "Book not available" 
        return "Available"