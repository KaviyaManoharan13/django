"""
This module contains utility functions for handling XYZ.
Describe the purpose or contents of this module here.
"""
from django.contrib import admin
from .models import(Contact)
from .models import(Department)
from .models import(Employee)

# Register your models here.
admin.site.register(Contact)
admin.site.register(Department)
admin.site.register(Employee)
