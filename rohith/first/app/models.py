from django.db import models

class new(models.Model):
    name=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    experienceyear=models.CharField(max_length=30)
    languages=models.CharField(max_length=30)