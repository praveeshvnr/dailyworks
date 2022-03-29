

# Create your models here.
from django.db import models

# Create your models here.
class addmore1(models.Model):
    name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    psw1 = models.CharField(max_length=20)
    psw2 = models.CharField(max_length=20,default='')
    interest = models.CharField(max_length=100,default='')

