from django import forms

from .models import Favourite_books

class FavBooksForm(forms.ModelForm):
    """
    Defines Form structure assosiated with the favourite boooks model
    """

    class Meta:
        model = Favourite_books
        fields = ('book_name', 'book_authors', 'book_category')
        labels = {
            "book_name": 'Favourite book',
            "book_authors": "Author",
            "book_category": "Category"
        }

    