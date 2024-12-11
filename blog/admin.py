from django.contrib import admin
from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'default_image')
    search_fields = ['category']


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'user',
        'slug',
        'category',
        'status',
        'created_on',
        'updated_on',
        'featured'
    )
    search_fields = ['title', 'content']
    list_filter = ('status', 'category', 'featured')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('user', 'post', 'approved', 'created_on', 'updated_on')
    search_fields = ['user_username', 'body']
    list_filter = ('approved', 'created_on')
    summernote_fields = ('body')
