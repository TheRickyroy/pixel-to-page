from . import views
from django.urls import path

# Common slug pattern for posts
post_pattern = '<slug:category_slug>/<slug:post_slug>/'

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:category_slug>/', views.category_view, name='category'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    path(post_pattern, views.post_detail, name='post_detail'),
    path(
        f'{post_pattern}comment/edit/<int:comment_id>/',
        views.comment_edit,
        name='comment_edit',
    ),
    path(
        f'{post_pattern}comment/delete/<int:comment_id>/',
        views.comment_delete,
        name='comment_delete',
    ),
]
