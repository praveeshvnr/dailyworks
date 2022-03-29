from django.db import models

# Create your models here.
class new(models.Model):
    name=models.CharField(max_length=30)
    dob=models.CharField(max_length=30)
    passwd=models.CharField(max_length=30)    
    email=models.EmailField(max_length=30)   
    year=models.EmailField(max_length=30)
    hobbies=models.CharField(max_length=100,default='')
class news(models.Model):
    id_new=models.AutoField(primary_key=True)
    clz=models.CharField(max_length=30)
    db=models.CharField(max_length=30)
    fr_id=models.ForeignKey(new, on_delete=models.CASCADE)