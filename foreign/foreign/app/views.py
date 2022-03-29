from django.shortcuts import render
from app.models import product,catagory
def home(request):
    data=product.objects.all()
    return render(request,'home.html',{'data':data})
def show(request,id_new):
    data=product.objects.get(id_new=id_new)
    return render(request,'show.html',{'data':data})
# Create your views here.
