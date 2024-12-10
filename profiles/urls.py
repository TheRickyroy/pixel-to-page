from django.urls import path
from .views import edit_profile, update_email, profile_view

urlpatterns = [
    path('edit/', edit_profile, name='edit-profile'),
    path('update-email/', update_email, name='update-email'),
    path('', profile_view, name='profile'), 
]