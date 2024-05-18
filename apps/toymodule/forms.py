from django.forms import ModelForm
from .models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    """CATEGORIES_CHOICES = (
        (1, "Baby Toys"),
        (2, "Cars and Bikes"),
        (3, "Dolls and Playsets"),
        (4, "Outdoors"),
        (5, "Others"),
    )
    
    name = forms.CharField(max_length = 100)
    image = forms.ImageField()
    price = forms.FloatField()
    category = forms.ChoiceField(choices=CATEGORIES_CHOICES)"""

class AddUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username','email','password1','password2']
        
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())