import datetime
from django.shortcuts import render
from event.models import Event, Showtime, PositionPrice,EventOrganizer
from promotion.models import Promotion
from event.views import get_type
from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseForbidden
# Create your views here.


def make_event_type_list(event_list):
    event_type_list = []
    for event in event_list:
        category = get_type(event.id)
        organizer = event.event_organizers.all()[0]
        dates = Showtime.objects.filter(event=event)
        position_price = PositionPrice.objects.get(organizer=organizer, event=event)
        total_capacity = 0
        for show_time in event.show_times.all():
            total_capacity += show_time.capacity
        if dates:
            event_type_list.append((event, category, organizer, dates, total_capacity, position_price.price))
        else:
            event_type_list.append((event, category, organizer, total_capacity, position_price.price))
    return event_type_list


def all_promotion(request):
    return render(request, 'all_promotion.html', {
        'logged_in': request.user.is_authenticated(),
        'events': make_event_type_list(Event.objects.all())

    })


def promotion(request, event_id):
    if request.user.is_authenticated() and request.user.is_organizer:
        if request.is_ajax():
            print("ajax")
            if request.POST.get('discount') != "" and request.POST.get('remaining') != "" and request.POST.getlist('times[]') != []:
                discount = (request.POST.get('discount', ''))
                remaining = (request.POST.get('remaining', ''))
                selected_show_times = request.POST.getlist('times[]', '')
                for selected_show_time in selected_show_times:
                    Promotion(showtime_id=selected_show_time, discount=discount, remaining=remaining, issued_time=datetime.datetime.now()).save()
                    # promotion.showtime = Showtime.objects.get(id=selected_show_time)
                return HttpResponse(1)
            else:
                print("error")
                return HttpResponse(0)
        else:
            event = Event.objects.get(id=event_id)
            organizers = EventOrganizer.objects.filter(event=event)
            organizers_showtimes = []
            for organizer in organizers:
                show_times = Showtime.objects.filter(organizer_id=organizer.id, event_id=event_id)
                organizers_showtimes.append((organizer, show_times))
            return render(request, 'promotion.html', {
                'logged_in': request.user.is_authenticated(),
                'organizers_showtimes': organizers_showtimes
            })
    else:
        return HttpResponseRedirect("/")