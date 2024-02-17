from django.shortcuts import render
from .models import artist

# Create your views here.
def artist(request):
    return render(request,"artist.html",)
