from django.db import models
class Product(models.Model):
    pname = models.CharField(max_length = 100)
    pimage = models.ImageField(blank=True, null=True, default='picture.png')
    pprice = models.FloatField()
    pcategory = models.CharField(max_length = 20, default = "Others")
    
    def __str__(self):
        return self.pname
    