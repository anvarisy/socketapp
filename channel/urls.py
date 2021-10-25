from django.urls import path

from . import views

urlpatterns = [
    path('', views.Homepage.as_view(), name='home'),
    path('room/', views.Roompage.as_view(), name='room'),
]