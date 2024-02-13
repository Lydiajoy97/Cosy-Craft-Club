from django.shortcuts import render, get_object_or_404

from django.views import generic
from .models import Uploads

# Create your views here.
class uploadsList(generic.TemplateView):
    template_name = "index.html"

def uploads_detail(request, slug):
    """
    Display an individual :model:`artwork.uploads`.

    **Context**

    ``post``
        An instance of :model:`artwork.uploads`.

    **Template:**

    :template:`artwork/uploads_detail.html`
    """

    queryset = uploads.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "artwork/uploads_detail.html",
        {"post": post},
    )