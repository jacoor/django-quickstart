from django.test import SimpleTestCase
from quickstart.books.models import Book
from freezegun import freeze_time


# Create your tests here.

class BookAvailiabilityTestCase(SimpleTestCase):
    def test_book_not_available(self):
        book = Book(
            full_title="Test full title",
            title="test title",
            is_available=False,
            return_date=None
        )

        assert book.check_availability() == "Book not available"
