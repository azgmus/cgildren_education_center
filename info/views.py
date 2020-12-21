from django.shortcuts import render
from django.views.generic.base import View

from .models import InfoPage

class InfoPageView(View):
    def get(self, request):
        info = InfoPage.objects.all()
        return render(request, 'base.html', {"info": info})