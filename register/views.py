from django.shortcuts import render,redirect
from django.contrib import messages
from apps.models import Account,user
from apps.views import navbar
from restswitch.models import Switch
# Create your views here.

def register(req):
    if(req.method=='POST'):
        email=req.POST["email"]
        username=req.POST["username"]
        first_name=req.POST["first_name"]
        last_name=req.POST["last_name"]
        country=req.POST["country"]
        phone_number=req.POST["phone_number"]
        password=req.POST["password"]
        confirm_password=req.POST["confirm_password"]
        if(Account.objects.filter(email=email).exists()):
            messages.error(req,"Email Id already exists")
        if(Account.objects.filter(username=username).exists()):
            messages.error(req,"Username already exists")
        if(password!=confirm_password):
            messages.error(req,"Passwords doesn't match")
        else:
            user1=Account.objects.create_user(email=email,username=username,first_name=first_name,last_name=last_name)
            user1.country=country
            user1.phone_number=phone_number
            user1.set_password(password)
            user1.save()
            obj1=Switch(id=user1.id,user=user1)
            obj1.save()
            return redirect('/login')
    else:
        return render(req,'register.html',navbar(req))
    return render(req,'register.html',navbar(req))