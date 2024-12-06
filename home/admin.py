from django.contrib import admin
from .models import Hero, Cta
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Hero)
class HeroAdmin(SummernoteModelAdmin):
    summernote_fields = ('hero_text',)
    list_display = ('hero_heading',)

@admin.register(Cta)
class CtaAdmin(SummernoteModelAdmin):
    summernote_fields = ('cta_text',)
    list_display = ('cta_heading',)