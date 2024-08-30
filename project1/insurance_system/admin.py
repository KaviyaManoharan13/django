"""admin for library management"""

from django.contrib import admin
from .models import InsurancePolicy, Customer, CustomerPolicy

admin.site.register(InsurancePolicy)
admin.site.register(Customer)
admin.site.register(CustomerPolicy)
# admin.site.register(Address)
