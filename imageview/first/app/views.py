# Create your views here.
from django.shortcuts import render
from app.models import new
# Create your views here.

def reg(request):
    return render(request, 'reg.html')


def save(request):
    
    if request.method == "POST":
        name1 = request.POST.get("name")
        dob  = request.POST.get("dob")
        password = request.POST.get("password")
        email  = request.POST.get("email")
        pict  = request.FILES["pic"]
        try:
            member = new(name=name1,dob=dob,password=password,email=email,pic=pict)
            member.save()
            return render(request, 'show.html',{'member':member})
        except:
            return render(request, 'reg.html')

    else:
         return render(request, 'reg.html')