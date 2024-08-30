"""urls for crud"""
from django.urls import path
from .views import get_image_base64

urlpatterns = [
    path('images/', get_image_base64, name='get-image'),
    # other URL patterns...
]
