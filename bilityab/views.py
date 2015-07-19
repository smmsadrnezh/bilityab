from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {
        'pageTitle': "bilityab",
    })

def terms(request):
    return render(request, 'terms.html', {
        # 'PageTitle': "bilityab",
    })


def about(request):
    return render(request, 'about.html', {
        # 'PageTitle': "bilityab",
    })


def contact(request):
    return render(request, 'contact-us.html', {})
