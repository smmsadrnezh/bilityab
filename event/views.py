from django.http import Http404
from django.shortcuts import render

from .models import *


# -*- coding: utf-8 -*-


def events(request):
    return render(request, 'all-events.html', {
        'logged_in': request.user.is_authenticated()

    })


def add_event(request, event_id):
    return render(request, 'add-event.html', {
        'logged_in': request.user.is_authenticated()

    })


def edit_event(request, event_id):
    return render(request, 'edit-event.html', {
        'logged_in': request.user.is_authenticated()

    })


def all_sport(request):
    return render(request, 'all-events.html', {
        'logged_in': request.user.is_authenticated()

    })


def all_music(request, event_id):
    return render(request, 'all-events.html', {
        'logged_in': request.user.is_authenticated()

    })


def all_cinema(request, event_id):
    return render(request, 'all-events.html', {
        'logged_in': request.user.is_authenticated()

    })


def all_tourism(request, event_id):
    return render(request, 'all-events.html', {
        'logged_in': request.user.is_authenticated()

    })


def sport(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
        teams = Sport.objects.get(event_id=event_id)
        print(teams)
    except Event.DoesNotExist:
        raise Http404("sport event does not exist!")
    return render(request, 'sport.html', {
        'title': event.title
    })


def tourism(request, event_id):
    return render(request, 'tourism.html', {
        'logged_in': request.user.is_authenticated()

    })


def cinema(request, event_id):
    return render(request, 'cinema.html', {
        'logged_in': request.user.is_authenticated()

    })


def music(request, event_id):
    return render(request, 'music.html', {
        'logged_in': request.user.is_authenticated()

    })


def all_organizer(request):
    return render(request, 'all-organizer.html', {
        'logged_in': request.user.is_authenticated()

    })


def organizer(request, organizer_id):
    return render(request, 'organizer.html', {
        'logged_in': request.user.is_authenticated()

    })


def report(request):
    return render(request, 'report.html', {'logged_in': request.user.is_authenticated()
    })