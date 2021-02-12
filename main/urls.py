from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.MainView.as_view()),
    path('schedule/<int:pk>/', views.ScheduleView.as_view()),
    path('info/<str:page_name>/', views.AboutView.as_view()),
    ]