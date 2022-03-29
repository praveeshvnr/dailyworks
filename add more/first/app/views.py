from django.shortcuts import render

# Create your views here.
from app.models import addmore1


def home(request):
    return render(request,'home.html')

def form(request):
    return render(request,'form.html')

def save1(request):

    if request.method == "POST":
        name = request.POST.get("name")
        psw1 = request.POST.get("psw1")
        psw2 = request.POST.get("psw2")
        Email = request.POST.get("Email")
        interest = request.POST.get("mytext[i]")
        
        
        try:
            member1 =addmore1(name=name, psw1=psw1, psw2=psw2, Email=Email, interest=interest)
            member1.save()
            return render(request,'form.html',{'member1':member1})
        except:
           return render(request,'form.html')
    else:
        return render(request, 'form.html')

# Create your views here.
