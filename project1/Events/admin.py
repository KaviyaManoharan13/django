""" this shows the admin page"""
from django.contrib import admin
from .models import Venue
from .models import Clubuser
from .models import Event

admin.site.register(Venue)
admin.site.register(Clubuser)
admin.site.register(Event)

# Register your models here.
