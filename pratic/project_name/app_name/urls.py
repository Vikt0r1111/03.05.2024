# app_name/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.stats_view, name='stats'),
]