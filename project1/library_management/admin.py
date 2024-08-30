"""admin for library management"""

from django.contrib import admin
from .models import Book, Student, Transaction, Address

admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Transaction)
admin.site.register(Address)
