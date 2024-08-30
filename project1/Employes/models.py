"""
This module contains Django models for the application.
Describe the purpose or contents of this module here.
"""
from django.db import models

# Create your models here.


class Contact(models.Model):
    """This class represents  Employee contact details"""

    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)


class Department(models.Model):
    """This class represents  Employee belongs to the department"""

    name = models.CharField(max_length=255)
    description = models.TextField()
    myfield = models.CharField(
        max_length=256, choices=[("1", "greencolor"), ("2", "redcolor")]
    )


class Employee(models.Model):
    """This class represents Employee details"""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.OneToOneField(
        Contact, on_delete=models.CASCADE
    )  # Assuming Contact is another model
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE
    )  # Assuming Department is another model

    def __str__(self):
        return self.first_name + "" + self.last_name

    # Your code ends here, and there are no extra blank lines below.
