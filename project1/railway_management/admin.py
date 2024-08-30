"""admin for railway_mangement"""
from django.contrib import admin
from .models import Train, Station, Route

admin.site.register(Train)
admin.site.register(Station)
admin.site.register(Route)
