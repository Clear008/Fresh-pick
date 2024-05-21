from django.utils import timezone  # Import the timezone module
from .models import CartItem  # Import the CartItem model

import json
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.management.base import BaseCommand
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.shortcuts import redirect, get_object_or_404

import random
import datetime
import time
import os

from .forms import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

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
            cart = Cart.objects.create(user=new_user, created_at=timezone.now())
            cart.save()
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

@login_required
def add_to_cart(request):
    # Your existing logic with some improvements:
    if request.method == 'POST':
        try:
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity', 1))  # Allow optional quantity

            product = Product.objects.get(pk=product_id)
            cart, created = Cart.objects.get_or_create(user=request.user, defaults={'created_at': timezone.now()})

            # Check for product availability
            if product.quantity_available < quantity:
                 return render(request, 'products.html', {'error': 'Product out of stock'})
                

            # Calculate total price based on quantity and product price
            total_price = quantity * product.price
            
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart, product=product, defaults={'quantity': quantity, 'price': product.price, 'price_total': total_price}
            )

            if not created:
                cart_item.quantity += quantity
                # Recalculate total price for existing item
                cart_item.price_total += total_price
                cart_item.save()

            # Update product quantity after successful addition
            product.quantity_available -= quantity
            product.save()
            cart_item.save()
            
            # Upon successful addition, redirect to the product listing page
            return redirect('products')

        except (ObjectDoesNotExist):
            return JsonResponse({'error': 'Invalid product'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def cart_items(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum([cart_item.price_total for cart_item in cart_items])
    return render(request, 'cart_items.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required
def remove_from_cart(request, cart_item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, pk=cart_item_id)
        product = cart_item.product
        product.quantity_available += cart_item.quantity
        product.save()
        cart_item.delete()
        return redirect('cart-items')
    return JsonResponse({'error': 'Invalid request'}, status=400)


