from django.test import TestCase
from quickstart.books.controllers import BooksController
from quickstart.books.models import Book
import pytest
from django.core.management import call_command

class BooksControllerAvailabilityTestCase(TestCase):
    def test_book_not_available(self):
        book = Book(
            full_title="Test full title",
            title="test title",
            is_available=False,
            return_date=None
        )
        controller = BooksController()

        assert controller.check_availability(book) == "Book not available"

    @pytest.fixture
    def load_books(self):
        call_command('loaddata', 'quickstart/books/tests/books', verbosity=0)

    @pytest.mark.usefixtures("load_books")
    def test_list_available_books(self):
        assert Book.objects.count() == 3
        controller = BooksController()
        available_books = controller.list_available_books()
        assert available_books.count() == 2
        assert all(book.is_available for book in available_books)