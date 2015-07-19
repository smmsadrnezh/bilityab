from django.shortcuts import render

# Create your views here.


def purchased(request, user_id):
    return render(request,'tickets.html',{

    })


def organized_events(request, user_id):
    return render(request, 'organized_events.html', {

    })