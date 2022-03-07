from django.test import Client, TestCase
from .models import Favourite_books

# Create your tests here.

client = Client()

class TestFavBookCreate(TestCase):
    """Test adding new book"""

    def setUp(self):
        """Setup app for testing"""

        fav_book_object = Favourite_books.objects.create(
            book_name='Hamlet',
            book_authors='Mark Burningspear',
            book_category='Shakespearian Play'
        )

        self.name_already_exists = {
            'book_name':'Hamlet',
            'book_authors':'Different Author',
            'book_category':'Shakespearian Play'
        }
        self.valid_data = {
            'book_name':'Carrying the Fire by Mike Collins',
            'book_authors':'Mike Collins',
            'book_category':'Apace exploration'
        }

    def test_create(self):
        current_length = len(Favourite_books.objects.all())
        Favourite_books.objects.create()
        new_length = len(Favourite_books.objects.all())
        self.assertEqual(new_length, current_length + 1 )
        print(current_length,'current length')
        print(new_length,' new length----')

    def tearDown(self) -> None:
        return super().tearDown()
       
