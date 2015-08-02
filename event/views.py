from .models import *
from django.http import Http404
from django.shortcuts import render

# -*- coding: utf-8 -*-


def events(request):
    return render(request, 'all-events.html', {

    })


def add_event(request, event_id):
    return render(request, 'add-event.html', {

    })


def edit_event(request, event_id):
    return render(request, 'edit-event.html', {

    })


def all_sport(request):
    return render(request, 'all-events.html', {

    })


def all_music(request, event_id):
    return render(request, 'all-events.html', {

    })


def all_cinema(request, event_id):
    return render(request, 'all-events.html', {

    })


def all_tourism(request, event_id):
    return render(request, 'all-events.html', {

    })


def sport(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("sport event does not exist")
    return render(request, 'sport.html', {
        'title': event.title
    })


def tourism(request, event_id):
    return render(request, 'tourism.html', {

    })


def cinema(request, event_id):
    return render(request, 'cinema.html', {

    })


def music(request, event_id):
    return render(request, 'music.html', {

    })


def all_organizer(request):
    return render(request, 'all-organizer.html', {

    })


def organizer(request, organizer_id):
    return render(request, 'organizer.html', {

    })


def report(request):
    return render(request, 'report.html', {})