from django.shortcuts import render, get_object_or_404

from django.views import generic
from .models import Uploads

# Create your views here.
def Uploads(request):
    template_name = "gallery.html"
def gallery(request, slug):
    """
    Display an individual :model:`artwork.gallery`.

    **Context**

    ``post``
        An instance of :model:`artwork.uploads`.

    **Template:**

    :template:`artwork/gallery.html`
    """

    queryset = uploads.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "artist/gallery.html",
        {"post": post},
        )

def login(request):
    template_name = "login.html"
    
    return render(
        request,
        "artist/login.html",
        {"post": post},
        )