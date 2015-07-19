from django.shortcuts import render

# Create your views here.


def all_sport(request, event_id):
    return render(request, 'all-sport.html', {

    })


def all_art(request, event_id):
    return render(request, 'all-art.html', {

    })


def entertainment(request, event_id):
    return render(request, 'tourism.html', {

    })


def movie(request, event_id):
    return render(request, 'movie.html', {

    })


def sport(request, event_id):
    return render(request, 'sport.html', {

    })


def concert(request, event_id):
    return render(request, 'concert.html', {

    })


def entertainment(request, event_id):
    return render(request, 'tourism.html', {

    })


def organizer(request, event_id):
    return render(request, 'organizer.html', {

    })

def organizer_events(request, event_id):
    return render(request, 'organizer-events.html', {

    })

def all_organizer(request, event_id):
    return render(request, 'all-organizer.html', {

    })

def add_event(request, event_id):
    return render(request, 'add-events.html', {

    })


def events(request):
    return render(request, 'all-events.html', {

    })


def edit_event(request, event_id):
    return render(request, '', {

    })


def organizer(request):
    return render(request, 'organizer.html', {})


def report(request):
    return render(request, 'report.html', {})