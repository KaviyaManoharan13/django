"""This that are available in db"""
import sys
from django.db import models



# Create your models here.
class Venue(models.Model):
    """This class defines the event venue"""

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=25)
    web = models.URLField()
    email = models.EmailField(max_length=25)

    # def __str__(self):
    #     """thIS RETURN THE STRING"""
    #     return self.name


class Clubuser(models.Model):
    """This class defines the clubuser"""

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=25)

    def __str__(self):
        """return strings"""
        return self.firstname + "" + self.lastname


class Event(models.Model):
    """EVENT"""

    event_name = models.CharField(max_length=100)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    event_date = models.DateTimeField()
    description = models.TextField()
    attendee = models.ManyToManyField(Clubuser)

    # def __str__(self):
    #     """ RETURN STRINGS"""
    #     return self.event_name
# 

