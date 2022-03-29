from django.shortcuts import render
from app.models import new
# Create your views here.
def reg(request):
    return render(request,'reg.html')
def save(request):
    member = new(name=request.POST['name'], dob=request.POST['dob'], passwd=request.POST['passwd'], email=request.POST['email'], year=request.POST['year'])
    member.save()
    return render(request,'db/home.html')