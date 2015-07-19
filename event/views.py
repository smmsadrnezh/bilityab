from django.shortcuts import render

# Create your views here.


def movie(request, event_id):
    return render(request, 'movie.html', {

    })


def sport(request, event_id):
    return render(request, 'sport-event.html', {

    })


def concert(request, event_id):
    return render(request, 'concert.html', {

    })


def entertainment(request, event_id):
    return render(request, 'entertainment.html', {

    })


def art(request, event_id):
    return render(request, 'art.html', {

    })


def organizer(request, event_id):
    return render(request, 'organizer.html', {

    })


def add_event(request, event_id):
    return render(request, 'add_event.html', {

    })


def events(request, event_id):
    return render(request, 'events.html', {

    })


def edit_event(request, event_id):
    return render(request, '', {

    })


def delete_event(request, event_id):
    return render(request, '', {

    })



