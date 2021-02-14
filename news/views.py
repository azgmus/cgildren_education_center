from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


class NewsListView(ListView):
    model = Article
    queryset = Article.objects.all()
    template_name = 'news.html'
