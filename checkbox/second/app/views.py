from django.http import HttpResponse
from django.shortcuts import render
from app.models import chkbox



# Create your views here.
def home(request):
    return render(request, 'home.html')

def savevalue(request):
    if request.method == 'POST':
        if request.POST.get('hobbies'):
            savedata = chkbox()
            savedata.hobbies = request.POST.get('hobbies')
            savedata.save()

            return render(request, 'home.html')
    else:
        return render(request, 'home.html')