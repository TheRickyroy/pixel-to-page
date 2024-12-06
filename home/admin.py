from django.contrib import admin
from .models import Hero, Cta, Info
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Hero)
class HeroAdmin(SummernoteModelAdmin):
    summernote_fields = ('heading', 'button_text', 'active')
    list_display = ('heading',)

@admin.register(Cta)
class CtaAdmin(SummernoteModelAdmin):
    summernote_fields = ('heading', 'button_text', 'active')
    list_display = ('heading',)

@admin.register(Info)
class CtaAdmin(SummernoteModelAdmin):
    summernote_fields = ('heading', 'button_text', 'active')
    list_display = ('heading',)