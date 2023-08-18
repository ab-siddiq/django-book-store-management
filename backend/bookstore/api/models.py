from django.db import models

# Create your models here.
class BookStoreModel(models.Model):
    CATEGORY = (
        ('Mystery','mystery'),
        ('Thriller','Thriller'),
        ('Sci-Fo','Sci-Fi'),
        ('Humor','Humor'),
        ('Horror','Horror'),
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    edition = models.CharField(max_length=20)
    category = models.CharField(choices=CATEGORY,max_length=30)
    publication_date = models.DateTimeField(auto_now_add=True)
    last_published = models.DateTimeField(auto_now=True)