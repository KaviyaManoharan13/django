"""This module contains Django models for email sending"""
from django.db import models


class EmailMessage(models.Model):
    """models representing email message"""

    subject = models.CharField(max_length=255)
    body = models.TextField()
    recipient = models.EmailField()
