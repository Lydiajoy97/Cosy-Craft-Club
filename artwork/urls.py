from . import views
from django.urls import path

urlpatterns = [
     path('', views.home, name= 'home'),
     path('', views.gallery, name= 'gallery'),
     path('', views.login, name='login'),
     
]