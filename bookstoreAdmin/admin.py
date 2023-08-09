from django.contrib import admin
from .models import *
# Register your models here.

class BookManager(admin.ModelAdmin):
    list_display = ['id','book_name','author_name','published_date']
    
admin.site.register(Book,BookManager)
