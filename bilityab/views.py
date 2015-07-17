from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {
        # 'PageTitle': "bilityab",
    })


def events(request):
    return render(request, 'sport-event.html', {
        # 'PageTitle': "bilityab",
    })


def organizer(request):
    return render(request, 'organizer.html', {})


def contact(request):
    return render(request, 'contact.html', {})
