from django.urls import path

from .views import delete_fav_book, home, fav_book_form,like_book

urlpatterns = [
    path('', home, name='home'),
    path('add', fav_book_form, name='add_fav_book'),
    path('<uuid:id>/', fav_book_form, name='edit_fav_book'),
    path('delete/<uuid:id>/', delete_fav_book, name='delete_fav_book'),
    path('like/<uuid:id>/', like_book, name='like_book')
]