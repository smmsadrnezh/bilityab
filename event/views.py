# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from event.models import Event,Categories
from bilityab.change_date import ChangeDate


def events(request):
    return render(request, 'all-events.html', {
        'logged_in': request.user.is_authenticated()

    })


def add_event(request):
    if request.user.is_authenticated():
        if request.is_ajax():
            if(request.POST.get('event-title', '') != "" and request.POST.get('event-description', '') != "" and request.POST.get('event-type', '') != "" and request.POST.get('event-capacity', '') != "" and request.POST.get('event-address', '') != ""):
                Event(title=request.POST.get('event-title', ''),
                    description=request.POST.get('event-description', ''),
                    category_id=request.POST.get('event-type', ''),
                    capacity=request.POST.get('event-capacity', ''),
                    address=request.POST.get('event-address', ''),
                    event_organizer_id=request.user.id,
                    photo="jingili.jpg"
                    ).save()
                return HttpResponse(1)
            else:
                return HttpResponse(0)
        else:
            return render(request, 'add-event.html', {
                'logged_in': request.user.is_authenticated(),
                'categories': Categories.objects.all()
            })
    else:
        return HttpResponseRedirect('/')


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
        show_time = event.show_times.all()[0]
        print(ChangeDate().get_persian_date(show_time.date))
    except Event.DoesNotExist:
        raise Http404("sport event does not exist!")
    return render(request, 'sport.html', {
        'event': event,
        # 'persian_date': ChangeDate.get_persian_date(show_time.date)
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
