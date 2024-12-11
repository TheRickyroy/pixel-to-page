from django.shortcuts import render
from .models import Hero, Cta, Signup, Info


def HomePage(request):
    # Fetch the active hero and CTA
    active_hero = Hero.objects.filter(is_active=True).first()
    active_cta = Cta.objects.filter(is_active=True).first()
    active_signup = Signup.objects.filter(is_active=True).first()
    active_info = Info.objects.filter(is_active=True).first()

    # Prepare context for rendering
    context = {
        'hero': active_hero,
        'cta': active_cta,
        'signup': active_signup,
        'info': active_info,
    }

    return render(request, 'home/index.html', context)
