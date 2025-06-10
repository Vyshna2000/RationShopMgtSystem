from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from eration.models import *
import hashlib
# from reportlab.pdfgen import canvas 
from django.views.generic import View


# Create your views here.

def index(request):
    return render(request,'index.html')

def loginuser(request):
    if request.method == "POST":
        email=request.POST['username']
        password=request.POST['password']
        #hashpassword=hashlib.md5(password.encode('utf8')).hexdigest()
        query=RegistrationDetail.objects.all().filter(email=email,password=password)
        if query:
            for x in query:
                request.session['userid'] = x.id
                request.session['useremail'] = x.email
                uid=request.session['userid']
            return HttpResponseRedirect('/home/')
        else:
            return render(request,'index.html')
    else:
        return render(request,'index.html')

def homeuser(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')

def productpage(request):
    return render(request,'products.html')

def servicespage(request):
    return render(request,'services.html')

def mailpage(request):
    if request.method == "POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        query=Contact_tb(name=name,phone=phone,email=email,subject=subject,message=message)
        query.save()
        return render(request,'mail.html')
    else:
        return render(request,'mail.html')

def householdpage(request):
    return render(request,'household.html')

def vegetablespage(request):
    return render(request,'vegetables.html')

def kitchenpage(request):
    return render(request,'kitchen.html')

def subscribe(request):
    if request.method == "POST":
        email=request.POST['email']
        query=Subscribe_tb(email=email)
        query.save()
        return render(request,'index.html')
    else:
        return render(request,'index.html')

def singleproduct(request):
    return render(request,'single.html')

def productlist(request):
    return render(request,'product_list.html')

def addproduct(request):
    if request.method == "POST":
        image=request.POST['image']
        name=request.POST['name']
        price=request.POST['price']
        quantity=request.POST['quantity']
        discription=request.POST['discription']
        query=Product_tb(image=image,name=name,price=price,quantity=quantity,discription=discription)
        query.save()
        return render(request,'add_product.html')
    else:
        return render(request,'add_product.html')



