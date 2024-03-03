from django.urls import path, re_path
from apps.toymodule import views

urlpatterns = [    
    path('', views.index, name='index'),
]
