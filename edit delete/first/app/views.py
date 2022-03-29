from django.shortcuts import redirect, render

from app.models import new
# Create your views here.

def show(request):
    vars=new.objects.all()
    return render(request,'show.html',{'var':vars})

def delete(request,id):
    vars1=new.objects.get(id=id)
    vars1.delete()
    return redirect('/show')

def edit(request,id):
    vars=new.objects.get(id=id)
    return render(request,'edit.html',{'vars':vars})

def update(request,id):
    vars=new.objects.get(id=id)
    vars.name=request.POST.get('name')
    vars.save()
    return redirect('/show')