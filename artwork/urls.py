from . import views
from django.urls import path

urlpatterns = [
    # path('', views.uploadsList.as_view(), name='home'),
     path('', views.home, name= 'home'),
     path('gallery/', views.gallery, name= 'gallery'),
     path('login/', views.login, name='login'),
     
]