"""urls for userprofile"""
from django.urls import path
from user_profile import views

urlpatterns = [
    path("user", views.home, name="home"),
    path("pdf/", views.gen_pdf, name="pdf"),
]
