from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:category_slug>/', views.category_view, name='category'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    path('<slug:category_slug>/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('<slug:category_slug>/<slug:post_slug>/comment/edit/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:category_slug>/<slug:post_slug>/comment/delete/<int:comment_id>', views.comment_delete, name='comment_delete'),
]