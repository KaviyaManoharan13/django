from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  gender = models.CharField(max_length=255)
  age = models.IntegerField()