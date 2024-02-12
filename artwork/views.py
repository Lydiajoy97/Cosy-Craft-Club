from django.shortcuts import render
from django.views import generic
from .models import Uploads

# Create your views here.
class UploadsList(generic.TemplateView):
  #  queryset = Uploads.objects.all()
    template_name = "index.html"
  #  paginate_by = 3