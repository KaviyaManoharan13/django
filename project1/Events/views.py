""" URL functionalities foe events"""
from django.shortcuts import render

# from django.http import HttpResponse
# from django.template import loader
from .models import Event

# Create your views here.
def all_event(request):
    """This DEFINE THE EVENT"""
    # import pdb;pdb.set_trace()
    event_list = Event.objects.all().order_by("event_date").values() # pylint: disable=no-member
    # template = loader.get_template('event.html')
    return render(request, "event.html", {"myevent": event_list})
