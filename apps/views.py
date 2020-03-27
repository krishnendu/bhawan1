from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout ,login as log_in
from .models import Account,user
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib import messages
#from .forms import BlogForm

def navbar(req):

    log='Log in'
    url='login'
    username='login'
    name='Krishnendu Chatterjee'
    phone_number='+917003033085'
    email='krishnenduchatterjee25@gmail.com'
    welcome=''
    authenticated=False
    admin=False
    if req.user.is_authenticated:
        log='Log out'
        url='logout'
        username=req.user.username
        admin=req.user.is_admin
        authenticated=req.user.is_authenticated
        welcome='Welcome '+username
    nav={ 'profile' : { 'name' : 'Profile' , 'username' : username , 'welcome' : welcome , 'admin' : admin, 'authenticated' : authenticated },
    'log' : { 'name' : log , 'url' : url},
    'register' : {'name' : 'Register' , 'url' : 'register'},
    'copyright' : { 'name' : name , 'phone_number' : phone_number , 'email' : email ,}
    }
    return nav

def home(req):
    return render(req,"home/index.html",navbar(req))