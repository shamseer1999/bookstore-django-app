from django.contrib import admin
from .models import *
# Register your models here.

class AdminManager(admin.ModelAdmin):
    list_display = ['id','name','username','email','phone','status']
    list_display_links = ['id','name']
    list_per_page = 10
    search_fields = ('name','username')
    
    fieldsets = (
        (None, {"fields": ("name","username","phone","email","status","is_staff","is_active")}),
        
    )
    
    
admin.site.register(Admin,AdminManager)
