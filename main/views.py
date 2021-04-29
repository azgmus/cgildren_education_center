
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import KidsGroup, InfoPages
from .forms import ContactForm
from django.contrib import messages


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'razvitiya.tsentr@list.ru', ['herodotus@inbox.ru'], fail_silently=False)
            return redirect('main')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})


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