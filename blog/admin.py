from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Post admin list from the walkthrough
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'excerpt', 'created_on', 'status')
    list_filter = ('status',)
    search_fields = ['title']
    summernote_fields = ('content',)
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Comment)
