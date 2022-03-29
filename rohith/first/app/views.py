from django.shortcuts import redirect, render

from app.models import new
# Create your views here.


def reg(request):
    vars=new.objects.all()
    return render(request,'reg.html',{'var':vars})

def show(request):
    vars=new.objects.all()
    return render(request,'show.html',{'vars':vars})

def delete(request,id):
    vars1=new.objects.get(id=id)
    vars1.delete()
    return redirect('/show')

def edit(request,id):
    vars=new.objects.get(id=id)
    return render(request,'edit.html',{'var':vars})

def update(request,id):
    vars=new.objects.get(id=id)
    vars.name=request.POST.get('name')
    vars.lastname=request.POST.get('lastname')
    vars.password=request.POST.get('password')
    vars.email=request.POST.get('email')
    vars.experienceyear=request.POST.get('experienceyear')
    vars.languages=request.POST.get('languages')


    vars.save()
    return redirect('/show')

def save(request):
        name=request.POST.get("name")
        lastname=request.POST.get("lastname")
        password=request.POST.get("password")
        email=request.POST.get("email")
        experienceyear=request.POST.get("experienceyear")
        languages=request.POST.get("languages")

        vars=new(name=name,lastname=lastname,password=password,email=email,experienceyear=experienceyear,languages=languages)
        vars.save()
        vars=new.objects.all()
        return render(request, 'show.html',{'vars':vars})