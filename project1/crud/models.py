# models.py
""" models for crud"""
from django.db import models

class Crudsqlite(models.Model):
    """ models representing image """
    image = models.ImageField(upload_to='images/')
