from django.db import models
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError

class Hero(models.Model):
    hero_image = CloudinaryField('image')
    hero_image_alt = models.TextField()
    hero_heading = models.CharField(max_length=200)
    hero_text = models.TextField()
    hero_button_text = models.CharField(max_length=200)
    hero_button_url = models.URLField()
    hero_button_label = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_active:
            # Deactivate all other heroes
            Hero.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

class Cta(models.Model):
    cta_image = CloudinaryField('image')
    cta_image_alt = models.TextField(blank=True)
    cta_heading = models.CharField(max_length=200)
    cta_text = models.TextField()
    cta_button_text = models.CharField(max_length=200)
    cta_button_url = models.URLField()
    cta_button_label = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_active:
            # Deactivate all other CTAs
            Cta.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)