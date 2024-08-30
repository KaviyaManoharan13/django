from django.urls import path
from . import views

urlpatterns = [
    path('policy', views.policy_list, name='policy_list'),
    path('register/<int:policy_id>/', views.register_policy, name='register_policy'),
    # Add other URLs as needed
]
