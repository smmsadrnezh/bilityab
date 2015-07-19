from django.shortcuts import render

# Create your views here.


def edit(request, promotion_id):
    return render(request, 'promotion.html', {

    })


def add(request):
    return render(request, '', {

    })


def remove(request, promotion_id):
    return render(request, '', {

    })