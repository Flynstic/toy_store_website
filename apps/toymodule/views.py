from django.shortcuts import render, redirect
from .models import User, Product

def index(request):
    # render the appropriate template for this request
    products = Product.objects.filter().order_by('pname')
    return render(request, 'toymodule/index.html', {'products':products})

def login(request):
    if request.method == "POST":
        mail = request.POST.get('email')
        passwd = request.POST.get('passwd') 
        checkEmail = User.objects.filter()
        for c in checkEmail:
            if c.email == mail:
                if c.password == passwd:
                    return redirect('addProduct')
                else:
                    error_messege = 'Email or password is incorrect!'
                    return render(request, 'toymodule/login.html', {'error_messege': error_messege})
        error_messege = 'Email or password is incorrect!'
        return render(request, 'toymodule/login.html', {'error_messege': error_messege})
        
    return render(request, 'toymodule/login.html')

def authorize(request):
    pass

def register(request):
    if request.method == "POST":
        mail = request.POST.get('email')
        passwd = request.POST.get('passwd')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        if mail == passwd == fname == lname == '':
            error_messege = 'Fields should not be empty!'
            return render(request, 'toymodule/register.html', {'error_messege': error_messege})
        if len(passwd) < 8:
            error_messege = 'Password should be more than 8 letters!'
            return render(request, 'toymodule/register.html', {'error_messege': error_messege})
        checkEmail = User.objects.filter()
        for c in checkEmail:
            if c.email == mail:
                error_messege = 'Account is already existing!'
                return render(request, 'toymodule/register.html', {'error_messege': error_messege})
        print(User.objects.filter(email__contains=mail))
        newuser = User.objects.create(email = mail, password = passwd, firstname = fname, lastname= lname)
        newuser.save()
        return render(request, 'toymodule/registerSuccess.html')
    
    return render(request, 'toymodule/register.html')

def addProduct(request):
    return render(request, 'toymodule/addProduct.html')

def babyToys(request):
    products = Product.objects.filter(pcategory__exact = 'Baby Toys').order_by('pname')
    return render(request, 'toymodule/babyToys.html', {'products':products})

def outdoors(request):
    products = Product.objects.filter(pcategory__exact = 'Outdoors').order_by('pname')
    return render(request, 'toymodule/outdoors.html', {'products':products})

def dollsAndPlaysets(request):
    products = Product.objects.filter(pcategory__exact = 'Dolls and Playsets').order_by('pname')
    return render(request, 'toymodule/dollsAndPlaysets.html', {'products':products})

def carsAndBikes(request):
    products = Product.objects.filter(pcategory__exact = 'Cars and Bikes').order_by('pname')
    return render(request, 'toymodule/carsAndBikes.html', {'products':products})
