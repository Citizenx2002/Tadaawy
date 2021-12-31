from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import reverse_related
from medicines.models import Medicines
# Create your models here.
class Diseases(models.Model):
    image=models.ImageField(upload_to='photo/%y/%m/%d',default='D:\tadaawy.jpg')
    name=models.CharField(max_length=100,primary_key=True)
    attribute =models.CharField(max_length=800)
    medicine=models.ForeignKey(Medicines,related_name='Medicines',on_delete=CASCADE)
    medicine2=models.ForeignKey(Medicines,related_name='Medicine2',on_delete=CASCADE,null=True,blank=True)
    medicine3=models.ForeignKey(Medicines,related_name='Medicines3',on_delete=CASCADE,null=True,blank=True)
    def __str__(self):
        return self.name

