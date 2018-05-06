from django.db import models

# Create your models here.
class book(models.Model):
    author_name = models.CharField(max_length=100)
    book_name = models.CharField(max_length=100)
    book_cover = models.FileField()

    def __str__(self):
        return self.book_name + ' - ' + self.author_name