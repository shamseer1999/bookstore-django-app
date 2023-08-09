from django.views import View
from django.shortcuts import render
from .models import *
from accounts.models import Admin
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
        
        
