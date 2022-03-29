from operator import mod
from pyexpat import model
from django.db import models

class catagory(models.Model):
    catagory=models.CharField(max_length=200)
    cart=models.CharField(max_length=200,default='00000')
    
class product(models.Model):
    id_new=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    catagory=models.ForeignKey(catagory,on_delete=models.CASCADE)
# Create your models here.
