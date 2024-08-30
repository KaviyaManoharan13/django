"""views for railway function"""
from django.shortcuts import render
from .models import Train, Station

def train_list(request):
    """request handles train list"""
    trains = Train.objects.all()# pylint: disable=E1101
    return render(request, "railway/train.html", {"trains": trains})


def station_list(request):
    """request handles station list"""
    stations = Station.objects.all()# pylint: disable=E1101
    return render(request, "railway/station_list.html", {"stations": stations})
