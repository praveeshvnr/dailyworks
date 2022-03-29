# Create your views here.
from django.shortcuts import render
from app.forms import inputForm
from app.models import new1
# Create your views here.

def reg(request):
    if request.method == "POST":
        form = inputForm(data=request.POST)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request,'home.html',{"obj":obj})
    else:
        form = inputForm()
    return render(request, 'form.html',{'form':form})

def show(request):
    return render(request,'show.html')