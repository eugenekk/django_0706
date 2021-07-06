from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'book'
urlpatterns = [
    path('', views.book_list, name="list"),
    path('new/', views.book_new, name="new"),
    path('<id>/edit/', views.book_edit, name="edit"),
    
]