from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, logout as log_out ,login as log_in
from apps.models import Account
from restapi.models import SwitchJson
from django.http import HttpRequest , JsonResponse , HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
#from restswitch.serializers import SwitchSerializer

import json

# Create your views here.

def authenticated(req):
    if(req.method=='GET'):
        if(req.user.is_authenticated ):
            return JsonResponse({"id" : req.user.id , "token" : req.user.token.hex } , status=200)
        else:
            return JsonResponse({"error" : "Not Authenticated"} , status=400)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def login(req):
    if(req.method=='POST'):
        data= JSONParser().parse(req)
        email = data['email']
        password = data['password']
        if(req.user.is_authenticated ):
            return JsonResponse({"id" : req.user.id , "token" : req.user.token.hex } , status=200)
        else:
            try:
                user = authenticate(req, email=Account.objects.get(username=email).email, password=password)
            except:
                user = authenticate(req, email=email , password=password)
            if user is not None:
                log_in(req, user)
                return JsonResponse({"id" : req.user.id , "token" : req.user.token.hex } , status=200)
            else:
                return JsonResponse({"error" : "Email/Username or Password does not match"} , status=400)

    else:
        return HttpResponse(status=400)


def logout(req):
    if(req.user.is_authenticated ):
        log_out(req)
        return JsonResponse({"messege" : "Log out Successfull"} , status=200)
    else:
        return JsonResponse({"error" : "No user to log out"} , status=400)


#api for switch

@csrf_exempt
def switch(req,token):
    if(Account.objects.filter(token=token).exists()):
        user=Account.objects.get(token=token)
        if req.method=='GET' :
            switch=SwitchJson.objects.get(id=user.id)
            return JsonResponse(switch.switch , safe=False , status=200)
        elif req.method=='PUT':
            data= JSONParser().parse(req)
            try:
                idnew=data['id']
                if(id!=idnew):
                    return JsonResponse({} , status=400)
            except:
                pass
            switch=SwitchJson.objects.get(id=user.id)
            try:
                if not valid_switch(data):
                    return JsonResponse({"error" : "Invalid Data Input"} , status=400)
                
                switch.switch.update(data)
                switch.switch=remove_none(switch.switch)
                switch.save()
                return JsonResponse(switch.switch , safe=False , status=200)
            except:
                return JsonResponse({"error" : "PUT request Failed"} , status=400)
        elif req.method=='PATCH':
            data= JSONParser().parse(req)
            try:
                idnew=data['id']
                if(id!=idnew):
                    return JsonResponse({} , status=400)
            except:
                pass
            switch=SwitchJson.objects.get(id=user.id)
            try:
                if not valid_switch(data):
                    return JsonResponse({"error" : "Invalid Data Input"} , status=400)
                switch.switch.update(data)
                switch.switch=remove_none(switch.switch)
                switch.save()
                return JsonResponse(remove_none(data) , safe=False , status=200)
            except:
                return JsonResponse({"error" : "PATCH request Failed"} , status=400)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)

#api for switch name
@csrf_exempt
def users_list(req):
    if(req.user.is_authenticated and req.user.is_admin) :
        if req.method=='GET':
            users={}
            for id,switch in SwitchJson.objects.values_list('id','switch',named=True):
                users[str(id)]=switch
            return JsonResponse(users , safe=False , status=200)
        elif req.method=='PUT':
            data= JSONParser().parse(req)
            try:
                id=data['id']
            except:
                return JsonResponse({"error" : "id not mentioned"} , status=400)
            if not(SwitchJson.objects.filter(id=id).exists()):
                return JsonResponse({"error" : "id not valid"} , status=400)
            switch=SwitchJson.objects.get(id=id)
            try:
                del(data['id'])
                switch.switch.update(data)
                switch.switch=remove_none(switch.switch)
                switch.save()
                return JsonResponse(switch.switch , safe=False , status=200)
            except:
                return JsonResponse({"error" : "PUT request Failed"} , status=400)
        elif req.method=='DELETE':
            data= JSONParser().parse(req)
            try:
                id=data['id']
            except:
                return JsonResponse({"error" : "id not mentioned"} , status=400)
            if not(SwitchJson.objects.filter(id=id).exists()):
                return JsonResponse({"error" : "id not valid"} , status=400)
            switch=SwitchJson.objects.get(id=id)
            switch.delete()
            return JsonResponse({"messege" : "User "+str(id)+" is deleted"}, status=200)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def switch_name(req):
    if(req.user.is_authenticated and req.user.is_admin) :
        if req.method=='GET':
            users={}
            for id,switch_name in SwitchJson.objects.values_list('id','switch_name',named=True):
                users[str(id)]=switch_name
            return JsonResponse(users , safe=False , status=200)
        elif req.method=='PUT':
            data= JSONParser().parse(req)
            try:
                id=data['id']
            except:
                return JsonResponse({"error" : "id not mentioned"} , status=400)
            if not(SwitchJson.objects.filter(id=id).exists()):
                return JsonResponse({"error" : "id not valid"} , status=400)
            switch=SwitchJson.objects.get(id=id)
            try:
                del(data['id'])
                switch.switch_name.update(data)
                switch.switch_name=remove_none(switch.switch_name)
                switch.save()
                return JsonResponse(switch.switch_name , safe=False , status=200)
            except:
                return JsonResponse({"error" : "PUT request Failed"} , status=400)
        elif req.method=='DELETE':
            data= JSONParser().parse(req)
            try:
                id=data['id']
            except:
                return JsonResponse({"error" : "id not mentioned"} , status=400)
            if not(SwitchJson.objects.filter(id=id).exists()):
                return JsonResponse({"error" : "id not valid"} , status=400)
            switch=SwitchJson.objects.get(id=id)
            switch.delete()
            return JsonResponse({"messege" : "User "+str(id)+" is deleted"}, status=200)
    else:
        return HttpResponse(status=400)


def remove_none(obj):
    newobj={}
    for i in obj:
        if not obj[i]==None :
            newobj.update({ i : obj[i] })
    return newobj

def valid_switch(obj):
    for i in obj:
        if(i[0]=='s' and obj[i] not in (True,False)):
            return False
        if(i[0]=='d' and (obj[i]<0 or obj[i]>255 )):
            return False
        if(i[0] not in ('s','d')):
            return False
    return True

