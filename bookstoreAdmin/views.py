from django.views import View
from django.shortcuts import render
from .models import *
from accounts.models import Admin
from django.views.generic import ListView
# Create your views here.

class HomeListView(View):
    
    def get(self,request):
        admins = Admin.objects.all()
        books = Book.objects.all()
        context = {
            'admins' : admins.count(),
            'books' : books.count()
        }
        
        return render(request,'mngr/index.html',context)
    
class AdminsListView(ListView):
    
    model = Admin
    template_name = 'mngr/admin/index.html'
    context_object_name = 'admins'
    paginate_by = 10
    
class BooksListView(ListView):
    
    model = Book
    template_name = 'mngr/books/index.html'
    context_object_name = 'books'
    paginate_by = 5
        
        
