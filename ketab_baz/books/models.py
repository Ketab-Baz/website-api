from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    goodreads_link = models.CharField(max_length=300)
    series = models.CharField(max_length=80)
    cover_link = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=100)
    author_goodreads_link = models.CharField(max_length=200)
    goodreads_average_rating = models.FloatField()
    number_of_pages = models.IntegerField()
    date_published = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    genre_and_votes = models.CharField(max_length=200)
    isbn = models.CharField(max_length=50)
    isbn13 = models.CharField(max_length=50)
    awards = models.CharField(max_length=1500)
    amazon_redirect_link = models.CharField(max_length=250)
    recommended_books = models.CharField(max_length=250)
    books_in_series= models.CharField(max_length=250)
    description = models.CharField(max_length=10000)

    def __str__(self):
        return self.title
