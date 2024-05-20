from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login,logout

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.management.base import BaseCommand
from django.conf import settings
import random
import datetime
import time
import os

# Create your views here.
def index(request):
    products = Product.objects.all()

    return render(request, 'index.html', {'products': products})

@login_required
def products(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        return render(request, 'products.html', {'products': products})
    else:
        return redirect('login')


def user_signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)  # Correct form instantiation
        if form.is_valid():
            new_user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone_number=form.cleaned_data['phone_number'],
                birth_date=form.cleaned_data['birth_date'],
                shipping_address=form.cleaned_data['shipping_address']
            )
            new_user.save()
            login(request, new_user)
            return redirect('/products')
        else:
            print(form.errors)
    else:
        form = UserForm()  # Correct form instantiation
    return render(request, 'signup.html', {"form": form})

def user_login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/products')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = loginForm()
    return render(request, 'signin.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')

