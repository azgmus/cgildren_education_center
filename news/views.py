from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


class NewsListView(ListView):
    model = Article
    queryset = Article.objects.all()
    paginate_by = 5
    template_name = 'news_list.html'


class NewsDetailView(DetailView):
    model = Article
    slug_field = 'id'
    template_name = 'article.html'