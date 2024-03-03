from django.shortcuts import render, redirect

def index(request):
    # render the appropriate template for this request
    return render(request, 'toymodule/index.html')