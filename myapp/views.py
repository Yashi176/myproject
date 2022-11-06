from email.policy import HTTP
from html.entities import name2codepoint
import http
from http.client import HTTPResponse
from itertools import product
from django.shortcuts import render, HttpResponse
from . models import ProductTable, User, cart
from datetime import datetime
# Create your views here.
def setsession(request,email, password):
    print("Inside set session")
    request.session['email']=email
    request.session['password']=password
    return HttpResponse("session is set")
def getsession(request):
    email=request.session['email']
    password=request.session['password']
    return {"email":email,"password":password}
def Home(request):
    if request.method=="GET":
        product=ProductTable.objects.all()
        out = getsession(request)
        print(out["email"])
        if out["email"]:
            return render(request,"index.html",{'email':out["email"], "product":product})
        else:
            return render(request,"index.html",{"product":product})
    elif request.method=="POST":
        id=request.POST['id']
        print(id)
        data=ProductTable.objects.get(id=id)
        print(data)
        # add="Indore"
        user=User.objects.get(id=id)
        cart.objects.create(userid=user,p_name=data.name,qty=1,p_price=data.price,t_price=data.price,dlvry_add="Indore")
        cart_p=cart.objects.all()
        print("in cart p",cart_p)
        return render(request,"cart.html",{"cart":cart_p})
def login(request):
    if request.method=="GET":
        print("i am inside get")
        return render(request,"login.html")
    elif request.method=="POST":
        print("i am inside post")
        n1=request.POST['Name']
        e1=request.POST['Email']
        p1=request.POST['Password']
        try:
            print("inside try")
            ouT=User.objects.get(Email=e1,Password=p1)
            print(ouT.Email)

            ott = setsession(request, e1, p1)
            print("I am inside ott",ott)
            product=ProductTable.objects.all()
            return render(request,'index.html',{'email':ouT.Email, "product":product})
        except:
            return render(request,'login.html')
def cart1(request):
    # id=request.POST['id']
    # print(id)
    # data=ProductTable.objects.get(id=id)
    # print(data)
    # user=User.objects.get(id=1)
    # out=cart.objects.create(userid=user,p_name=data.name,qty=1,p_price=data.price,t_price=data.price,dlvry_add='Indore')   
    cart_p=cart.objects.all()
    return render(request,"cart.html",{"cart": cart_p})
def SignUp(request):
    if request.method == "GET":
        print("I am inside get method")
        return render(request,"Signup.html")
    elif request.method == "POST":
        print("I am inside post method")
        name = request.POST['Name']
        email = request.POST['Email']
        phone = request.POST['Phone']
        passw = request.POST['Password']
        cpassw = request.POST['cnf']
        print(name)
        print(email, phone, passw, cpassw)
        if passw == cpassw:
            User.objects.create(Name = name, Email = email, Phone_no = phone, Password = passw, CreatedAt = datetime.now())
            return render(request,"login.html")
        else:
            return render(request,"SignUp.html")