from django.shortcuts import render
from app.models import new,news

# Create your views here.
def reg(request):
    return render(request,'reg.html')
def saved(request):
    return render(request,'saved.html')
def reg2(request):
    return render(request,'reg2.html')
def save(request):
    member = new(name=request.POST['name'], dob=request.POST['dob'], passwd=request.POST['passwd'], email=request.POST['email'], year=request.POST['year'], hobbies=request.POST['hobbies'],)
    member.save()
    return render(request,'reg2.html',{'member':member})

def savek(request,id):
    member=new.objects.get(id=id)
    if request.method=="POST":
        clzl=request.POST.get("clz")
        db=request.POST.get("db")
        id_new=new.objects.get(id=id)
        try:
            member1=news(clz=clzl,db=db,fr_id=id_new)
            member1.save()
            return render(request, 'saved.html',{'member1':member1,'member':member})
        except:
            return render(request,'reg2.html')
    else:
        return render(request,'reg2.html')