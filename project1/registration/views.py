"""views functions for registration"""
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import UserProfile

def signup(request):
    """handle POST method"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # '''Check if user with the given username already exists'''
        if User.objects.filter(username=username).exists():
            return render(request, 'registration/signup.html', {'error': 'Username already exists'})
        
        # '''Create the user'''
        user = User.objects.create_user(username=username, email=email, password=password)
        user_profile = UserProfile.objects.create(user=user, activation_code='some_activation_code_here')
        return redirect('login')
    return render(request, 'registration/signup.html')

def user_login(request):
    """handle POST method"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')
