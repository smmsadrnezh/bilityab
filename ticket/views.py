from django.shortcuts import render
from ticket.models import PurchasedTicket
from django.http import HttpResponseRedirect

def buy(request, event_id):
    return render(request, 'buy.html', {
        'logged_in': request.user.is_authenticated()

    })


def ticket(request, user_id, purchased_id):
    return render(request, 'ticket.html', {
        'logged_in': request.user.is_authenticated()

    })


def all_ticket(request, user_id):
    if int(user_id) == request.user.id:
        return render(request, 'all-ticket.html', {
            'logged_in': request.user.is_authenticated(),
            'tickets': PurchasedTicket.objects.filter(user_id=request.user.id)
        })
    else:
        return HttpResponseRedirect('/')