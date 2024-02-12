from . import views
from django.urls import path

urlpatterns = [
     path('artwork/', views.UploadsList.as_view(), name='home'),
]