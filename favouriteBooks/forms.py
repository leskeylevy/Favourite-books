from django import forms

from favouriteBooks.models import Favourite_books

class FavBooksForm(forms.ModelForm):
    """
    Defines Form structure assosiated with the favourite boooks model
    """

    class Meta:
        model = Favourite_books
        fields = '__all__'