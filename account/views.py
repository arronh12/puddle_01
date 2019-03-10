from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User


def home(request):
    context = {
    }
    return render(request, 'account/home.html', context)


def login(request):
    context = {
        'user': User
    }
    return render(request, 'account/login.html', context)


def login_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...


