# -*- coding: utf-8 -*-
import datetime
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseForbidden

from bilityab.views import make_event_type_list, get_type
from bilityab.change_date import ChangeDate
from event.models import Event, Categories, Sport, Movie, Concert, EventRating, EventOrganizer


def events(request):
    return render(request, 'all-events.html', {
        'logged_in': request.user.is_authenticated(),
        'event_type_list': make_event_type_list(Event.objects.all())

    })


def add_event(request):
    if request.user.is_authenticated() and request.user.is_organizer:
        if request.is_ajax():
            # insert event and it's additional information to database
            if (request.POST.get('event-title', '') != "" and request.POST.get('event-description',
                                                                               '') != "" and request.POST.get(
                    'event-type', '') != "" and request.POST.get('event-capacity', '') != "" and request.POST.get(
                    'event-address', '') != ""):
                event = Event(title=request.POST.get('event-title', ''),
                              description=request.POST.get('event-description', ''),
                              category_id=request.POST.get('event-type', ''),
                              capacity=request.POST.get('event-capacity', ''),
                              address=request.POST.get('event-address', ''),
                              event_organizer_id=request.user.id,
                              photo="jingili.jpg"
                )
                event.save()
                if (request.POST.get('event-home-team', '') != "" and request.POST.get('event-away-team', '') != ""):
                    Sport(
                        event_id=event.id,
                        away_team=request.POST.get('event-home-team', ''),
                        home_team=request.POST.get('event-away-team', '')
                    ).save()
                elif (request.POST.get('event-director', '') != "" and request.POST.get('event-actors',
                                                                                        '') != "" and request.POST.get(
                        'event-year', '') != "" and request.POST.get('event-story-summary', '') != ""):
                    Movie(
                        event_id=event.id,
                        director=request.POST.get('event-director', ''),
                        actors=request.POST.get('event-actors', ''),
                        year=request.POST.get('event-year', ''),
                        story_summary=request.POST.get('event-story-summary', '')
                    ).save()
                elif (request.POST.get('event-vocalist', '') != "" and request.POST.get('event-musicians',
                                                                                        '') != "" and request.POST.get(
                        'event-music-group', '') != ""):
                    Concert(
                        event_id=event.id,
                        group_name=request.POST.get('event-music-group', ''),
                        vocalist=request.POST.get('event-vocalist', ''),
                        musicians=request.POST.get('event-musicians', '')
                    ).save()

                # redirect to site homepage
                return HttpResponse(1)
            else:
                # raise exception to user
                return HttpResponse(0)
        else:
            # add new event template for organizer
            return render(request, 'add-event.html', {
                'logged_in': request.user.is_authenticated(),
                'categories': Categories.objects.all()
            })
    else:
        return HttpResponseRedirect('/')


def edit_event(request, event_id):
    if request.user.is_authenticated() and request.user.is_organizer:
        type = get_type(Event.objects.get(id=event_id).id)
        if (type == "music"):
            return render(request, 'edit-event.html', {
                'logged_in': request.user.is_authenticated(),
                'categories': Categories.objects.all(),
                'event': Event.objects.get(id=event_id),
                'type': type,
                'concert': Concert.objects.get(event_id=event_id),
            })
        elif (type == "cinema"):
            return render(request, 'edit-event.html', {
                'logged_in': request.user.is_authenticated(),
                'categories': Categories.objects.all(),
                'event': Event.objects.get(id=event_id),
                'type': type,
                'movie': Movie.objects.get(event_id=event_id)
            })
        elif (type == "sport"):
            return render(request, 'edit-event.html', {
                'logged_in': request.user.is_authenticated(),
                'categories': Categories.objects.all(),
                'event': Event.objects.get(id=event_id),
                'type': type,
                'sport': Sport.objects.get(event_id=event_id),
            })
        else:
            return render(request, 'edit-event.html', {
                'logged_in': request.user.is_authenticated(),
                'categories': Categories.objects.all(),
                'event': Event.objects.get(id=event_id),
                'type': type,
            })

    else:
        return HttpResponseRedirect('/')


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
        event_date_time = datetime.datetime.combine(show_time.date, show_time.from_time)
    except Event.DoesNotExist:
        raise Http404("sport event does not exist!")
    return render(request, 'sport.html', {
        'event': event,
        'persian_date': ChangeDate().get_persian_date(show_time.date),
        'from_time': show_time.from_time,
        'remaining_time': int((event_date_time - datetime.datetime.now()).total_seconds() * 1000),
        'logged_in': request.user.is_authenticated(),
        'organizer': event.event_organizers.all()[0]
    })


def tourism(request, event_id):
    return render(request, 'tourism.html', {
        'logged_in': request.user.is_authenticated()

    })


def cinema(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
        event_rates = event.rates.all()
        can_rate = request.user.is_authenticated()
        rates_average = 0
        num_of_votes = len(event_rates)
        if num_of_votes:
            rates_sum = 0
            for rate in event_rates:
                rates_sum += rate.rate
                can_rate = can_rate and not (rate.user.id == request.user.id)
            rates_average = rates_sum / num_of_votes
    except Event.DoesNotExist:
        raise Http404('cinema event does not exist!')
    return render(request, 'cinema.html', {
        'logged_in': request.user.is_authenticated(),
        'event': event,
        'num_of_votes': num_of_votes,
        'rates_average_percent': rates_average * 20,
        'can_rate': can_rate
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
        'organizer': EventOrganizer.objects.get(id=organizer_id),
        'organizer_events': make_event_type_list(Event.objects.filter(event_organizers__id=organizer_id)),
        'logged_in': request.user.is_authenticated()
    })


def report(request):
    return render(request, 'report.html', {'logged_in': request.user.is_authenticated()
    })


def rate_event(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            if 'rate' in request.POST:
                rate = int(request.POST['rate'])
                if rate > 5 or rate < 0:
                    print('sada;dw')
                    return HttpResponseForbidden('invalid rate')
                event_id = request.POST['event_id']
                try:
                    event = Event.objects.get(pk=event_id)
                    EventRating.objects.get(event=event, user=request.user)
                    return HttpResponseForbidden('already rated')
                except Event.DoesNotExist:
                    return HttpResponseForbidden('invalid event id')
                except EventRating.DoesNotExist:
                    EventRating.objects.create(event=event, user=request.user, rate=rate)
                    return HttpResponse('success')
        else:
            return HttpResponseForbidden('post required')
    else:
        return HttpResponseForbidden('login required')


def get_sold_seats(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        event = Event.objects.get(pk=event_id)
        tickets = []
        for i in event.show_times.all()[0].tickets.all():
            tickets.extend(i.positions.all())
        return HttpResponse(tickets)
    else:
        return HttpResponseForbidden('post required')
