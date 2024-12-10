from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """
    Stores user profiles related to :midel: 'auth.User'
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    image = CloudinaryField('image', transformation=[{
        'width': 300, 
        'height': 300, 
        'crop': "fill"
        }
    ])
    bio = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    author_status = models.BooleanField(default=False)

    def __str__(self):
        return self.display_name