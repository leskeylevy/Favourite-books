import datetime
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Favourite_books
from .forms import FavBooksForm


# Create your views here.
def home(request):
    """
    List favourite books here  
    """
    fav_books = Favourite_books.objects.all()
    timenow = datetime.datetime.now().strftime("%H:%M:%S")
    context = {
        'fav_books': fav_books,
        "time": timenow
    }
    return render(request, 'favouriteBooks/index.html', context)


def fav_book_form(request,id=None):
    """
    Function that will handle create new fav_books
    """
    fav_book_form = FavBooksForm()
    if request.method == 'GET':
        if id is None:
            fav_book_form = FavBooksForm()
        else:
            favourite_book = Favourite_books.objects.get(pk=id)
            fav_book_form = FavBooksForm(instance=favourite_book)
        
        context = {
            'fav_book_form': fav_book_form
        }
        return render(request, 'favouriteBooks/form.html', context)

    else:
        if id is None:
            fav_book_form = FavBooksForm(request.POST)
        else:
            Favourite_book = Favourite_books.objects.get(pk=id)
            fav_book_form =FavBooksForm(request.POST, instance=Favourite_book)

        if fav_book_form.is_valid():
            fav_book_form.save()
            return redirect('home')

            # messages.success(request, ('Your Favourite Book has been added successfuly'))
        else:
            error = fav_book_form.errors
            message = f'There was an error creating your Favourite Book {error}'

        return HttpResponse(message)


def delete_fav_book(request,id):
    """"""
    Favourite_book = Favourite_books.objects.get(pk=id)
    Favourite_book.delete()

    return redirect('home')

def like_book(request,id):
    """"""
    Favourite_book = Favourite_books.objects.get(pk=id)
    Favourite_book.favourites = Favourite_book.favourites + 1
    Favourite_book.save()

    return redirect('home')
