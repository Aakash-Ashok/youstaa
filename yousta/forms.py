from django import forms
from yousta.models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2","phone","address"]


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class CatergoryCreateForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=["name"]