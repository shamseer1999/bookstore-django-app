from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.HomeListView.as_view(),name='mngr_home')
]
