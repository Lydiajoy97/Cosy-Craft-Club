from django.shortcuts import render, get_object_or_404

from django.views import generic
from .models import Uploads

# Create your views here.
class UploadsList(generic.TemplateView):
    template_name = "index.html"

def Uploads_detail(request, slug):
    """
    Display an individual :model:`Artwork.Uploads`.

    **Context**

    ``post``
        An instance of :model:`Artwork.Uploads`.

    **Template:**

    :template:`artwork/Uploads_detail.html`
    """

    queryset = Uploads.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "artwork/Uploads_detail.html",
        {"post": post},
    )