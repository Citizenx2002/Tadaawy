from django.db import models


# Create your models here.

class Medicines(models.Model):
    image=models.ImageField(upload_to='photo/%y/%m/%d',null=True,blank=True,default='D:\tadaawy.jpg')
    name=models.CharField(max_length=100)
    attribute =models.CharField(max_length=600)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    active=models.BooleanField(default=True,)
    def __str__(self) :
        return self.name