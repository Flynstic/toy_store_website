from django.urls import path, re_path
from apps.toymodule import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('baby-toys', views.babyToys),
    path('outdoors', views.outdoors),
    path('dolls-and-playsets', views.dollsAndPlaysets),
    path('cars-and-bikes', views.carsAndBikes),
    path('login', views.login),
    path('register', views.register),
]
