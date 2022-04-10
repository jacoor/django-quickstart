from django.test import SimpleTestCase
from django.urls import is_valid_path
from quickstart.books.controllers import BookController
from quickstart.books.models import Book


class BookControllerAvailabilityTestCase(SimpleTestCase):
    def test_book_not_available(self):
        book = Book(
            full_title="Test full title",
            title="test title",
            is_available=False,
            return_date=None
        )
        controller = BookController()

        assert controller.check_availability(book) == "Book not available"

