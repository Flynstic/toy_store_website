from django.shortcuts import render, redirect
from .models import User, Product

def index(request):
    # render the appropriate template for this request
    products = Product.objects.filter()
    return render(request, 'toymodule/index.html', {'products':products})

def login(request):
    return render(request, 'toymodule/login.html')

def authorize(request):
    pass

def register(request):
    if request.method == "POST":
        mail = request.POST.get('email')
        passwd = request.POST.get('passwd')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        print(mail, passwd)
        newuser = User.objects.create(email = mail, password = passwd, firstname = fname, lastname= lname)
        newuser.save()
        return render(request, 'toymodule/registerSuccess.html')
    
    return render(request, 'toymodule/register.html')

def babyToys(request):
    products = Product.objects.filter(pcategory__exact = 'Baby Toys')
    return render(request, 'toymodule/babyToys.html', {'products':products})

def outdoors(request):
    products = Product.objects.filter(pcategory__exact = 'Outdoors')
    return render(request, 'toymodule/outdoors.html', {'products':products})

def dollsAndPlaysets(request):
    products = Product.objects.filter(pcategory__exact = 'Dolls and Playsets')
    return render(request, 'toymodule/dollsAndPlaysets.html', {'products':products})

def carsAndBikes(request):
    products = Product.objects.filter(pcategory__exact = 'Cars and Bikes')
    return render(request, 'toymodule/carsAndBikes.html', {'products':products})
