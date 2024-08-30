"""Sample program for polls"""
from django.db import models

# Create your models here.


class Question(models.Model):
    """Functions specifies the Questions"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # def __str__(self):
    #     return f"{self.question_text}"


class Choice(models.Model):
    """This represent the choices for the quesions"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # def __str__(self):
    #     return f "{self.choice_text}"
