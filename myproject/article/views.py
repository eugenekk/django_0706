# from myproject import article
from django.db.models import fields
from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.
def article_list(request):
    print(request.user)
    qs = Article.objects.all()
    q = request.GET.get('q') # client 가 보낸 검색창 입력값
    if q:
        qs = qs.filter(title__icontains=q)
    return render(request, 'article/article_list.html', {'article_list' : qs, 'q':q})

def detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, "article/article_detail.html", {'article': article})

article_new = CreateView.as_view(model=Article, fields="__all__")

article_edit = UpdateView.as_view(model=Article, fields="__all__")

article_delete = DeleteView.as_view(model=Article, success_url = reverse_lazy("article:list"))