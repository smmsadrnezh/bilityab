from django.shortcuts import render

# Create your views here.


def buy(request, event_id):
    return render(request, 'buy.html', {

    })


def ticket(request, user_id, purchased_id):
    return render(request, 'ticket.html', {

    })
