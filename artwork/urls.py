from . import views
from django.urls import path

urlpatterns = [
     path('', views.uploadsList.as_view(), name='home'),
     path('<slug:slug>/', views.uploads_detail, name='uploads_detail'),
]