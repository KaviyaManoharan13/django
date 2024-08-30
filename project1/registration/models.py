"""This module contains Django models for registration"""
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    """By using a OneToOneField, each UserProfile instance is associated with exactly one User 
    instance, allowing you to extend the User model without modifying its structure directly."""
    # user = models.OneToOneField(User, on_delete=models.CASCADE)  # pylint: disable=E1101
    activation_code = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
