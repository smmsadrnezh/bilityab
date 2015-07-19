from django.shortcuts import render


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


def all_art(request, event_id):
    return render(request, 'all-events.html', {

    })


def all_tourism(request, event_id):
    return render(request, 'all-events.html', {

    })


def sport(request, event_id):
    return render(request, 'sport.html', {

    })


def tourism(request, event_id):
    return render(request, 'tourism.html', {

    })


def art(request, event_id):
    if event_id == 1:
        return render(request, 'movie.html', {

        })
    elif event_id == 2:
        return render(request, 'concert.html', {

        })


def all_organizer(request, event_id):
    return render(request, 'all-organizer.html', {

    })


def organizer(request, event_id):
    return render(request, 'organizer.html', {

    })


def report(request):
    return render(request, 'report.html', {})