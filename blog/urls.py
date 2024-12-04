from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:category_slug>/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('<slug:category_slug>/<slug:post_slug>/comment/<int:comment_id>/edit/', views.comment_edit, name='comment_edit'),
    path('<slug:category_slug>/<slug:post_slug>/comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]