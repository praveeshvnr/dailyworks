from django.db import models

# Create your models here.
class chkbox(models.Model):
    hobbies=models.CharField(max_length=100)