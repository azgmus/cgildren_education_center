from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.MainView.as_view(), name='main'),
    path('schedule/<int:pk>/', views.ScheduleView.as_view()),
    path('info/<str:page_name>/', views.AboutView.as_view()),
    path('contact_form', views.contact_form)
    ]