"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('profile/',views.profile),
    path('regkerala/',views.regkerala),
    path('explore/',views.explore),
    path('thrissure/',views.thrissure),
    path('alappuzha/',views.alappuzha),
    path('tvm/',views.tvm),
    path('vayanad/',views.vayanad),
    path('palakkad/',views.palakkad),
    path('save/',views.save),
    path('log/',views.log),
    path('login/',views.login),
    path('idukki/',views.idukki)


]
