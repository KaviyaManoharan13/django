from django.db import models
from django.contrib.auth.models import User

class InsurancePolicy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    contact_number = models.CharField(max_length=20)
    policies = models.ManyToManyField(InsurancePolicy, through='CustomerPolicy')

    def __str__(self):
        return self.user.username

class CustomerPolicy(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    policy = models.ForeignKey(InsurancePolicy, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.user.username} - {self.policy.name}"
