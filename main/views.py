from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import KidsGroup, InfoPages


class MainView(ListView):
    model = KidsGroup
    queryset = KidsGroup.objects.all()
    template_name = 'home.html'


class ScheduleView(View):
    def get(self, request, pk):
        group = KidsGroup.objects.get(id=pk)
        return render(request, 'schedule.html', {'group': group})


class AboutView(View):
    def get(self, request, page_name):
        page = InfoPages.objects.get(name=page_name)
        return render(request, 'about.html', {'page': page})