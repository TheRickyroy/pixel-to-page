from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author','slug', 'status', 'created_on', 'updated_on', 'featured')
    search_fields = ['title']
    list_filter = ('status', 'featured',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Comment)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('author', 'approved', 'created_on', 'updated_on')
    search_fields = ['title']
    list_filter = ('approved',)
    summernote_fields = ('body',)

