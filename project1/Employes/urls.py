"""
This module contains functions related to employes.
And the URL are mention here.
"""
from django.urls import path
#from django.urls import include, path

from.import views

urlpatterns= [
     path('employee_det',views.EmployeeView.as_view()),
]# Your code ends here
