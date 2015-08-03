# -*- coding: utf-8 -*-
from django.shortcuts import render

from event.models import Event, Categories, EventOrganizer


def get_type(event_id):
    sub_category = Categories.objects.get(id=event_id)
    category = Categories.objects.get(id=sub_category.parent_id).title
    return {
        'ورزشی': 'sport',
        'سینمایی': 'cinema',
'موسیقی'         : 'music',
        'گردشگری': 'tourism'
    }[category]


def make_event_type_list(event_list):
    event_type_list = []
    for item in event_list:
        category = get_type(item.category.id)
        organizer = EventOrganizer.objects.filter(event__id=item.id)
        event_type_list.append((item, category, organizer))
    return event_type_list


def home(request):
    return render(request, 'home.html', {
        'bestEvents': make_event_type_list(Event.objects.all()[:3]),
        'nearestEvents': make_event_type_list(Event.objects.all()[:3]),
        'actionMovies': make_event_type_list(Event.objects.filter(category__title='اکشن')),
        'dramaticMovies': make_event_type_list(Event.objects.filter(category__title='درام')),
        'comicMovies': make_event_type_list(Event.objects.filter(category__title='کمدی')),
        'volleyballEvents': make_event_type_list(Event.objects.filter(category__title='والیبال')),
        'footballEvents': make_event_type_list(Event.objects.filter(category__title='فوتبال')),
        'basketballEvents': make_event_type_list(Event.objects.filter(category__title='بسکتبال')),
        'wrestleEvents': make_event_type_list(Event.objects.filter(category__title='کشتی')),
        'zooEvents': make_event_type_list(Event.objects.filter(category__title='باغ وحش')),
        'amusementEvents': make_event_type_list(Event.objects.filter(category__title='شهر بازی')),
        'circusEvents': make_event_type_list(Event.objects.filter(category__title='سیرک')),
        'traditionalMusic': make_event_type_list(Event.objects.filter(category__title='سنتی')),
        'popMusic': make_event_type_list(Event.objects.filter(category__title='پاپ')),
        'suggestedEvents': make_event_type_list(Event.objects.all()[:3]),
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
