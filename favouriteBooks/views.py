import datetime
from django.shortcuts import redirect, render
from django.contrib import messages

from .models import Favourite_books
from .forms import FavBooksForm


# Create your views here.
def home(request):
    """
    Function to render homepage    
    """
    fav_books = Favourite_books.objects.all()
    timenow = datetime.datetime.now().strftime("%H:%M:%S")
    context = {
        'fav_books': fav_books,
        "time": timenow
    }
    return render(request, 'favouriteBooks/index.html', context)


def add_fav_book(request):
    """
    Function that will handle create new fav_books
    """
    if request.method == 'POST':
        fav_book_form = FavBooksForm(request.POST)
        if fav_book_form.is_valid():
            fav_book_form.save()
            messages.success(request, ('Your Favourite Book has been added successfuly'))
        else:
            messages.error(request, 'There was an Error saving your Book')

        return redirect('favouriteBooks/index.html')

    context = {
        
    }
    return render(request, 'favouriteBooks/add.html', context)
            