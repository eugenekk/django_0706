from django.urls import path
from . import views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article

app_name = 'article'
urlpatterns = [
    path('', ListView.as_view(model=Article), name = 'list'),
    path('<pk>/detail/', DetailView.as_view(model=Article), name ='detail'),
    path('new/', views.article_new, name='new'),
    path('<pk>/edit/', views.article_edit, name='edit'),
    path('<pk>/delete/', views.article_delete, name="delete"),
]