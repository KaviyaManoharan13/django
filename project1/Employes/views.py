"""
This module contains Django models for the application.
Describe the purpose or contents of this module here.
"""
# from django.shortcuts import render
from django.http import HttpResponse
# import json
# from django.template import loader
from django.http import JsonResponse
from rest_framework.views import APIView
from Employes.models import Employee

# from .models import Contact


class EmployeeView(APIView):
    """This class represents EmployeeView."""

    def get(self, request):
        """This function retrieves employee data."""
        employee_list = list(
            Employee.objects.select_related("department", "contact").values(
                "first_name", "last_name", "department__name", "contact__phone"
            )
        )
        # Convert the list of dictionaries into a string representation
        response_data = '\n'.join([f"{employee['first_name']} {employee['last_name']}, {employee['department__name']}, {employee['contact__phone']}" for employee in employee_list])
        # Return the response
        return HttpResponse(response_data, content_type='text/plain')
    def post(self, request):
        """This function does somethinG Employeeview"""
        Employee.objects.create(# pylint: disable=no-member
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            phone=request.data["contact__phone"],
            department=request.data["department__name"],
        )# pylint: disable=no-member

    # end of the code
