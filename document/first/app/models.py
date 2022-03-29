# Create your models here.
from django.db import models

# Create your models here.
class new1(models.Model):
    name=models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    passwd = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    experience = models.CharField(max_length=30)