from django.urls import path
from . import views

urlpatterns = [
    path("", views.InfoPageView.as_view())
]