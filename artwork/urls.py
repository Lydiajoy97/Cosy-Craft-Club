from . import views
from django.urls import path

urlpatterns = [
     path('', views.uploadsList.as_view(), name='home'),
     path('gallery/', views.gallery, name='gallery'),
     path('login/', views.gallery, name='login'),
     path('', views.home, name= 'home'),
     path('', views.gallery, name= 'gallery'),
     path('', views.login, name='login'),
     
]