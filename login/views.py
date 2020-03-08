from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout as log_out ,login as log_in
from apps.models import Account
from apps.views import navbar


def login(req):
    if(req.method=='POST'):
        email = req.POST['email']
        password = req.POST['password']
        try:
            user = authenticate(req, email=Account.objects.get(username=email).email, password=password)
        except:
            user = authenticate(req, email=email , password=password)
        if user is not None:
            log_in(req, user)
            return redirect('/profile')
        else:
            messages.error(req,"Username or Password does not match")
            return render(req,'login.html',navbar(req))

    else:
        return render(req,'login.html',navbar(req))


def logout(req):
    log_out(req)
    return redirect('/')