from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Responseneed,Responseneed1
from pymongo import MongoClient
client=MongoClient("mongodb://127.0.0.1:27017/")
db=client['DOCTOR']
coll=db.details
def sample(request):
    return render(request,"cy_app/full_page.html")


def getres(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phno=request.POST.get('phone')
        email=request.POST.get('email')
        date=request.POST.get('date')
        db.coll.insert_one({'name': name, 'email': email, 'phone': phno,'date':date})
        c = Responseneed(name=name,email=email)
        c.save()
        return HttpResponse("SAVED")
    return HttpResponse("NOT SAVED")
def signup(request):
    return render(request,"cy_app/signup.html")

def signin(request):
    return render(request,"cy_app/signin.html")

def postsignup(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        passwo=request.POST.get('passwo')
        db.coll.insert_one({'fname':fname,'lname':lname,'email':email
                            ,'passwo':passwo})
        c=Responseneed1(fname=fname,lname=lname,email=email,passwo=passwo)
        c.save()
        return render(request,"cy_app/signin.html")
    else:
        return render(request,"cy_app/singup.html")

def checkuser(request):
    if request.method=='POST':
        email=request.POST.get('email')
        passwo=request.POST.get('passwo')

        c=db.coll.find_one({'email':email})

        if c['email']==email and c['passwo']==passwo:
             return render(request,"cy_app/full_page.html")
        else:
            return render(request,"cy_app/signin.html")
    return render(request,"cy_app/signin.html")
