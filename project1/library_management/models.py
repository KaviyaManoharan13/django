"""This module contains Django models for registration"""
from django.db import models


class Address(models.Model):
    """models representing Address"""

    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country}"


class Student(models.Model):
    """models representing Student"""

    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    """models representing Book"""

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=50)
    publication_date = models.DateField()
    available = models.BooleanField(default=True)
    objects = models.Manager()

    def __str__(self):
        return f"{self.title}"


class Transaction(models.Model):
    """models representing Transaction"""

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.book} - {self.student}"
