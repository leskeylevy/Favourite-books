from django.urls import path

from .views import home, add_fav_book

urlpatterns = [
    path('', home, name='home'),
    path('add', add_fav_book, name='add_fav_book')
]