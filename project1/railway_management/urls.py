"""urls for railway_management"""
from django.urls import path
from . import views

urlpatterns = [
    # path('railway', views.home, name='home'),
    path('trains/', views.train_list, name='train_list'),
    path('stations/', views.station_list, name='station_list'),
    # Add more paths for specific functionalities
]
