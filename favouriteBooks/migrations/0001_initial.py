# Generated by Django 4.0.3 on 2022-03-06 09:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='favourite_books',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('book_name', models.CharField(max_length=150)),
                ('book_authors', models.CharField(max_length=300)),
                ('book_category', models.CharField(max_length=100, null=True)),
                ('favourites', models.IntegerField(default=0)),
            ],
        ),
    ]
