from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=250)
    author_name = models.CharField(max_length=255)
    description = models.TextField()
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.book_name
