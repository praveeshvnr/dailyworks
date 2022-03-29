

# Create your views here.
from django.shortcuts import render,redirect
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator

from django.core import serializers
from django.http import JsonResponse

def home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        posts=Post.objects.filter(title__icontains=q)
    else:
        posts=Post.objects.all()
    # Pagintion
    paginator=Paginator(posts,30)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    return render(request,'home.html',{'posts':posts_obj})

# Add Method
def add(request):
    if request.method=='POST':
        title=request.POST['title']
        detail=request.POST['detail']
        Post.objects.create(title=title,detail=detail)
        messages.success(request,'Data has been added')
    return render(request,'add.html')

# Update Method
def update(request,id):
    if request.method=='POST':
        title=request.POST['title']
        detail=request.POST['detail']
        Post.objects.filter(id=id).update(title=title,detail=detail)
        messages.success(request,'Data has been updated')
    post=Post.objects.get(id=id)
    return render(request,'update.html',{'post':post})

# Delete Method
def delete(request,id):
    Post.objects.filter(id=id).delete()
    return redirect('home.html')

# Load More