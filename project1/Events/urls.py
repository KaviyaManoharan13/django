""" This url defines the Events"""
from django.urls import path
from . import views

urlpatterns = [
    path("events", views.all_event, name='all_event'),  # Corrected line
]
