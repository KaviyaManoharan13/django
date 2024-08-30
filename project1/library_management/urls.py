"""urls for library management"""
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('book/', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('student/', views.student_list, name='student_list'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    # Add URLs for CRUD operations
]
