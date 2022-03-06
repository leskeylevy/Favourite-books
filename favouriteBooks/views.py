import datetime
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render

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
    fav_book_form = FavBooksForm
    if request.method == 'POST':
        fav_book = FavBooksForm(request.POST)
        if fav_book.is_valid():
            fav_book.save()
            return redirect('home')

            # messages.success(request, ('Your Favourite Book has been added successfuly'))
        else:
            error = fav_book.errors
            message = f'There was an error creating your Favourite Book {error}'

        return HttpResponse(message)

    context = {
        'fav_book_form': fav_book_form
    }
    return render(request, 'favouriteBooks/add.html', context)
            