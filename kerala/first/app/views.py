from django.shortcuts import render
from app.models import new,new1

# Create your views here.
def index(request):
    return render(request,'index.html')
def profile(request):
    return render(request,'profile.html')
def regkerala(request):
    return render(request,'regkerala.html')
def explore(request):
    return render(request,'explore.html')
def thrissure(request):
    return render(request,'thrissure.html')
def palakkad(request):
    return render(request,'palakkad.html')
def tvm(request):
    return render(request,'tvm.html')
def alappuzha(request):
    return render(request,'alappuzha.html')
def vayanad(request):
    return render(request,'vayanad.html')
def idukki(request):
    return render(request,'idukki.html')

def save(request):
    member = new(name=request.POST['name'], email=request.POST['email'], password=request.POST['password'])
    member.save()
    return render(request,'profile.html')
def log(request):
    member = new1(name1=request.POST['name1'], password1=request.POST['password1'])
    member.save()
    return render(request,'index.html')


def login(request):
    if request.method=='POST':
        if new.objects.filter(name=request.POST['name1'], password=request.POST['password1']).exists():
            members= new.objects.get(name=request.POST['name1'], password=request.POST['password1'])
            return render(request, 'index.html',{'member':members})
        else:
            return render(request,'profile.html')

    else:
         return render(request,'profile.html')


