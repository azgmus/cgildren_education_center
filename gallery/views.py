from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Picture


class GalleryListView(ListView):
    model = Picture
    queryset = Picture.objects.all().order_by('id')
    paginate_by = 5
    template_name = 'gallery.html'