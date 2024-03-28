from django.db import models

class User(models.Model):
    email = models.CharField(max_length = 25)
    password = models.CharField(max_length = 25)
    firstname = models.CharField(max_length = 25)
    lastname = models.CharField(max_length = 25)
    

class Product(models.Model):
    pname = models.CharField(max_length = 100)
    pimage = models.ImageField()
    pprice = models.FloatField()
    pcategory = models.CharField(max_length = 20, default = "Others")
    