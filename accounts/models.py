from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.

class customUserManager(BaseUserManager):
    
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_("The username field is must"))
        user = self.model(username = username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, password, **extra_fields):
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        return self.create_user(username, password, **extra_fields)
    
class Admin(AbstractUser):
    CHOICES = (
        (1,'active'),
        (2,'inactive')
    )
    username = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100)
    status = models.IntegerField(choices=CHOICES,default=1)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    objects = customUserManager()
    
    def __str__(self):
        return self.username
    