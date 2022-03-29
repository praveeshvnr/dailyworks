from django.shortcuts import loader
from django.http import HttpResponse

# Create your views here.
def bgimg(request):
    temp=loader.get_template('bgimg.html')
    return HttpResponse(temp.render())
def star(request):
    return HttpResponse("<h1>Hello world</h1>")

