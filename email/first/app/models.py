from django.db import models

# Create your models here.


class em(models.Model):
    mail=models.EmailField(max_length=30)