from django.shortcuts import render,redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'home.html')
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'mail not')
                return render(request,'register.html')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1,email=email)
                user.save()
                print("user created")
                return render(request,'login.html')
        else:
            messages.info(request,'password not')
            return render(request,'register.html')

    else:
        return render(request,'register.html')
        

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return render(request,'home2.html')
        else:
            messages.info(request,'email taken')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'register.html')
def second(request,id):
    
    return render(request,'second.html')
def hello(request):
    return render(request,'home.html')
def home2(request):
    return render(request,'home2.html')