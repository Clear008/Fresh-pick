from django import forms
from .models import *

class UserForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    phone_number = forms.CharField(max_length=255)
    birth_date = forms.DateField()
    shipping_address = forms.CharField(max_length=255)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)


class loginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
