from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.HomeListView.as_view(),name='mngr_home'),
    path('admins',views.AdminsListView.as_view(),name='admins_list'),
    path('books',views.BooksListView.as_view(),name='books_list'),
]
