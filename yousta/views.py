from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import *
from yousta.forms import *
from yousta.models import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
# Create your views here.


class SignUpView(CreateView):
    template_name="yousta/signup.html"
    model=User
    form_class=RegistrationForm
    success_url=reverse_lazy("login")

    def form_valid(self,form):
        messages.success(self.request,"Account Created")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,"Failed to Create Account")
        return super().form_valid(form)


class LoginView(FormView):
    template_name="yousta/login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            usr=authenticate(self.request,username=username,password=password)
            if usr:
                login(self.request,usr)
                messages.success(request,"login successful")
                return redirect("signup")
            else:
                messages.error(request,"Login failed")
                return render(request,"login.html",{"form":form})
            

class CategoryCreateView(CreateView):
    template_name="yousta/category/create.html"
    form_class=CatergoryCreateForm
    model=Category
    success_url=reverse_lazy("category-create")

    def form_valid(self,form):
        messages.success(self.request,"Added Succesfully")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,"Failed to Add Category")
        return super().form_valid(form)