from django.shortcuts import render, redirect

def index(request):
    # render the appropriate template for this request
    return render(request, 'toymodule/index.html')

def login(request):
    return render(request, 'toymodule/login.html')

def register(request):
    return render(request, 'toymodule/register.html')

def babyToys(request):
    return render(request, 'toymodule/babyToys.html')

def outdoors(request):
    return render(request, 'toymodule/outdoors.html')

def dollsAndPlaysets(request):
    return render(request, 'toymodule/dollsAndPlaysets.html')

def carsAndBikes(request):
    return render(request, 'toymodule/carsAndBikes.html')