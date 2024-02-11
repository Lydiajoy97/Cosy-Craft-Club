from . import views
from django.urls import path

urlpatterns = [
    path('', views.UploadsList.as_view(), name='home'),
]