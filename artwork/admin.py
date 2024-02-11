from django.contrib import admin
from .models import Uploads, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Uploads)
class PostAdmin(SummernoteModelAdmin):
    fields: [
        'title',
        'image',
        'description',
        'artist'
    ]

# Register your models here.
admin.site.register(Comment)
