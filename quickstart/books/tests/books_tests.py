from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import FirefoxOptions
from selenium import webdriver

from django.core.management import call_command
import pytest

class BooksListTestCase(StaticLiveServerTestCase):

    @pytest.fixture
    def load_books(self):
        call_command('loaddata', 'quickstart/books/tests/books', verbosity=0)
    
    def setUp(self):
        super().setUp()
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        self.selenium = webdriver.Firefox(options=opts)

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    @pytest.mark.usefixtures("load_books")
    def test_books_list(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/books/'))
        books_list = self.selenium.find_elements_by_xpath('//*[@id="books"]/li')
        assert len(books_list) == 3
        