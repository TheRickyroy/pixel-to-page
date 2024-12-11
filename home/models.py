from django.db import models
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError


class Hero(models.Model):
    image = CloudinaryField('image')
    image_alt = models.TextField()
    heading = models.CharField(max_length=200)
    text = models.TextField()
    button_text = models.CharField(max_length=200)
    button_url = models.URLField()
    button_label = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_active:
            # Deactivate all other heroes
            Hero.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)


class Cta(models.Model):
    image = CloudinaryField('image')
    image_alt = models.TextField()
    heading = models.CharField(max_length=200)
    text = models.TextField()
    button_text = models.CharField(max_length=200)
    button_url = models.URLField()
    button_label = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_active:
            # Deactivate all other Call To Actionss
            Cta.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)


class Signup(models.Model):
    image = CloudinaryField('image')
    image_alt = models.TextField()
    heading = models.CharField(max_length=200)
    text = models.TextField()
    button_text = models.CharField(max_length=200)
    button_url = models.URLField()
    button_label = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_active:
            # Deactivate all other Signups
            Signup.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)


class Info(models.Model):
    image = CloudinaryField('image', transformation=[
        {'width': 300, 'height': 300, 'crop': "fill"}
        ])
    image_alt = models.TextField()
    heading = models.CharField(max_length=200)
    text = models.TextField()
    button_text = models.CharField(max_length=200)
    button_url = models.URLField()
    button_label = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_active:
            # Deactivate all other Infos
            Info.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)
