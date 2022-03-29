from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('show/',views.show),
    path('update/<int:id>',views.update),
]