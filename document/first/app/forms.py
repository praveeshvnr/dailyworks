import builtins
from django import forms
from django.forms import fields, models
from .models import new1

class inputForm(forms.ModelForm):
    class Meta:
        model=new1
        fields="__all__"