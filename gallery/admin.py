from django.contrib import admin
from .models import Uploads, Comment
from django_summernote.admin import SummernoteModelAdmin


# Post admin list from the walkthrough
@admin.register(Uploads)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('image', 'artist', 'description')
    list_filter = ('status',)
    search_fields = ['artist', 'name']
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Comment)
