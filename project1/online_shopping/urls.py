''' urls for online shopping'''
from django.urls import path
from . import views

urlpatterns = [
    path('product', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
