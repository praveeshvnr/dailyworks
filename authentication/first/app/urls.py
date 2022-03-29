from django.urls import re_path
from  .import views


urlpatterns = [
    re_path(r'^register$',views.register,name='register'),
    re_path(r'^login$',views.login,name='login'),
    re_path(r'^second/(?P<id>\d+)$',views.second,name='second'),
    re_path(r'^index$',views.index,name='home'),
    re_path(r'^login$',views.login,name='login'),
    re_path(r'^logout$',views.logout,name='logout'),
    re_path(r'^hello$',views.hello,name='hello'),
    re_path(r'^home2$',views.home2,name='hello'),
    
]