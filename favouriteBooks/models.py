import uuid
from django.db import models

# Create your models here.
class Favourite_books(models.Model):
    """
    structure for our favourite books class/Object
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    book_name = models.CharField(max_length=150, unique=True)
    book_authors = models.CharField(max_length=300)
    book_category = models.CharField(max_length=100, null=True)
    favourites = models.IntegerField(default=0)
