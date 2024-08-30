""" views representing online shoppings"""
from django.shortcuts import render
from .models import Product

def product_list(request):
    '''request handling product_list'''
    products = Product.objects.all()# pylint: disable=E1101
    return render(request, 'online_shopping/product_list.html', {'products': products})

def product_detail(request, product_id):
    '''request handling product_details'''
    product = Product.objects.get(id=product_id)# pylint: disable=E1101
    return render(request, 'online_shopping/product_details.html', {'product': product})
