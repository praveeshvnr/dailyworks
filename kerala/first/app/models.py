from django.db import models

# Create your models here.
class new(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)    
    email=models.EmailField(max_length=30)  

class new1(models.Model):
    name1=models.CharField(max_length=30)
    password1=models.CharField(max_length=30)    
