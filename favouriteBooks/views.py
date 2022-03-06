from django.http import HttpResponse
from django.shortcuts import render
import datetime

from favouriteBooks.models import Favourite_books


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