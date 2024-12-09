from django.contrib import admin
from .models import Hero, Cta, Signup, Info
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Hero)
class HeroAdmin(SummernoteModelAdmin):
    summernote_fields = ('text')
    list_display = ('heading', 'button_text', 'button_url', 'is_active')

@admin.register(Cta)
class CtaAdmin(SummernoteModelAdmin):
    summernote_fields = ('text')
    list_display = ('heading', 'button_text', 'button_url', 'is_active')

@admin.register(Signup)
class SignupAdmin(SummernoteModelAdmin):
    summernote_fields = ('text')
    list_display = ('heading', 'button_text', 'button_url', 'is_active')

@admin.register(Info)
class CtaAdmin(SummernoteModelAdmin):
    summernote_fields = ('text')
    list_display = ('heading', 'button_text', 'button_url', 'is_active')