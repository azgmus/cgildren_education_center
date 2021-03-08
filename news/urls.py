from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.NewsListView.as_view(), name='News'),
    path("<int:pk>/", views.NewsDetailView.as_view()),
    ]