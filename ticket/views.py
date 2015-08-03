from django.shortcuts import render
from django.http import HttpResponseRedirect

from ticket.models import PurchasedTicket
from event.models import Event, Showtime
from ticket.models import TicketPosition
from bilityab.views import get_type


def buy(request, event_id):
    return render(request, 'buy.html', {
        'logged_in': request.user.is_authenticated()

    })


def ticket(request, user_id, purchased_id):
    if int(user_id) == request.user.id:
        # find ticket and related event
        ticket = PurchasedTicket.objects.get(id=purchased_id)
        showtime = Showtime.objects.get(id=ticket.showtime_id)
        event = Event.objects.get(id=showtime.event_id)
        postitions = TicketPosition.objects.filter(ticket_id=purchased_id)

        # make list from event, event category and ticket
        ticket_event_type_list = []
        ticket_event_type_list.append((ticket, event, get_type(event.id), showtime, postitions))

        return render(request, 'ticket.html', {
            'logged_in': request.user.is_authenticated(),
            'ticket_event_type_list': ticket_event_type_list
        })
    else:
        return HttpResponseRedirect('/')


def all_ticket(request, user_id):
    if int(user_id) == request.user.id:
        return render(request, 'all-ticket.html', {
            'logged_in': request.user.is_authenticated(),
            'tickets': PurchasedTicket.objects.filter(user_id=request.user.id)
        })
    else:
        return HttpResponseRedirect('/')