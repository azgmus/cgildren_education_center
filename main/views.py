from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from django.views.generic import ListView
from .models import KidsGroup

class MainView(ListView):
    model = KidsGroup
    queryset = KidsGroup.objects.all()
    template_name = 'home.html'
