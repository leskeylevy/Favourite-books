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
    print(fav_books)
    return HttpResponse(content=f'Hello World the time in Nairobi now is {timenow}')