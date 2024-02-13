from . import views
from django.urls import path

urlpatterns = [
     path('', views.UploadsList.as_view(), name='home'),
     path('<slug:slug>/', views.Uploads_detail, name='uploads_detail'),
]