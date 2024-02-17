from django.contrib import admin
from .models import artist
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(artist)
class ArtistAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)