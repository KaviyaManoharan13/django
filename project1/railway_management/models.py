"""module representing railway management"""
from django.db import models


class Train(models.Model):
    """models representing trains"""

    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} "


class Station(models.Model):
    """models representing stations"""

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} "


class Route(models.Model):
    """models representing Route"""

    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
