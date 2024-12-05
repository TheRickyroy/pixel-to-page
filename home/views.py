from django.shortcuts import render
from .models import Hero, Cta

def HomePage(request):
    # Fetch the active hero and CTA
    active_hero = Hero.objects.filter(is_active=True).first()
    active_cta = Cta.objects.filter(is_active=True).first()

    # Prepare context for rendering
    context = {
        'hero': active_hero,
        'cta': active_cta,
    }

    return render(request, 'home/index.html', context)