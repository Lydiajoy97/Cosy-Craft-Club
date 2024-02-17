from django.shortcuts import render
from .models import artist

# Create your views here.
def artist(request):
    """
    Renders the artist page
    """
    about = artist.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "artist/artist.html",
        {"post": post},
        )