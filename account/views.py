from django.shortcuts import render

# Create your views here.


def profile_edit(request, user_id):
    return render(request, 'profile.html', {

    })


def charge(request, user_id):
    return render(request, 'charge.html', {

    })