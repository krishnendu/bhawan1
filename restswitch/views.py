from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpRequest , JsonResponse , HttpResponse
from rest_framework.parsers import JSONParser
from .models import Switch
from apps.models import Account
from .serializers import SwitchSerializer
from django.views.decorators.csrf import csrf_exempt

def profile(req):
    if not req.user.is_authenticated :
        return redirect('%s?next=%s' % (settings.LOGIN_URL, req.path))
    obj=list(Switch.objects.filter(user__id=req.user.id).values())
    #print(obj[0])
    return render(req,'demo/index.html',{ "user" : obj[0]})

def remove_none(obj):
    newobj={}
    for i in obj:
        if not obj[i]==None :
            newobj.update({ i : obj[i] })
    return newobj

# Create your views here.
@csrf_exempt
def users_list(req):
    if req.method=='GET':
        users=Switch.objects.all()
        serializer = SwitchSerializer(users, many=True)
        return JsonResponse([remove_none(i)for i in serializer.data] , safe=False)
    elif req.method=='POST':
        data= JSONParser().parse(req)
        id=data['id']
        if(Switch.objects.filter(id=id).exists()):
            user=Switch.objects.get(id=id)
            serializer = SwitchSerializer(user, data=data)
        else:
            serializer = SwitchSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(remove_none(serializer.data) , status=201)
        else:
            return JsonResponse(serializer.errors , status=400)

@csrf_exempt
def switch(req,id):
    user=Switch.objects.filter(id=id)
    if(user.exists()):
        if req.method=='GET' :
            users=Switch.objects.get(id=id)
            serializer = SwitchSerializer(users)
            return JsonResponse(remove_none(serializer.data) , safe=False)
        elif req.method=='PUT':
            data= JSONParser().parse(req)
            try:
                idnew=data['id']
                if(id!=idnew):
                    return JsonResponse({} , status=400)
            except:
                pass
            user=Switch.objects.get(id=id)
            serializer = SwitchSerializer(user, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(remove_none(serializer.data) , status=201)
            else:
                return JsonResponse(serializer.errors , status=400)
        elif req.method=='DELETE':
            user.delete()
            return HttpResponse(status=204)
        else:
            return JsonResponse({} , status=400)

    elif req.method=='POST':
        data= JSONParser().parse(req)
        try:
            idnew=data['id']
            if(id!=idnew):
                return JsonResponse({} , status=400)
        except:
            pass
        user=Switch.objects.create(id=id,user=Account.objects.get(id=id))
        serializer = SwitchSerializer(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(remove_none(serializer.data) , status=201)
        else:
            return JsonResponse(serializer.errors , status=400)

    else :
        return JsonResponse({},status=400)
