# -*- coding: utf-8 -*-
from django.shortcuts import render

from event.models import Event


def home(request):
    return render(request, 'home.html', {
        'bestEvents': Event.objects.all(),
        'nearestEvents': Event.objects.all(),
        'actionMovies': Event.objects.filter(category__title='اکشن'),
        'dramaticMovies': Event.objects.filter(category__title='درام'),
        'comicMovies': Event.objects.filter(category__title='کمدی'),
        'volleyballEvents': Event.objects.filter(category__title='والیبال'),
        'footballEvents': Event.objects.filter(category__title='فوتبال'),
        'basketballEvents': Event.objects.filter(category__title='بسکتبال'),
        'wrestleEvents': Event.objects.filter(category__title='کشتی'),
        'zooEvents': Event.objects.filter(category__title='باغ وحش'),
        'amusementEvents': Event.objects.filter(category__title='شهر بازی'),
        'circusEvents': Event.objects.filter(category__title='سیرک'),
        'traditionalMusic': Event.objects.filter(category__title='سنتی'),
        'popMusic': Event.objects.filter(category__title='پاپ'),
        'logged_in': request.user.is_authenticated()

    })


def terms(request):
    return render(request, 'terms.html', {
        'pageTitle': " - شرایط و ضوابط",
        'logged_in': request.user.is_authenticated()

    })


def about(request):
    return render(request, 'about.html', {
        'pageTitle': " - درباره",
        'logged_in': request.user.is_authenticated()

    })


def contact(request):
    return render(request, 'contact-us.html', {
        'pageTitle': " - تماس با ما",
        'logged_in': request.user.is_authenticated()

    })
