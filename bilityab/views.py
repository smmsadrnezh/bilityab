from django.shortcuts import render
# -*- coding: utf-8 -*-

def home(request):
    return render(request, 'home.html', {
    })


def terms(request):
    return render(request, 'terms.html', {
        'pageTitle': " - شرایط و ضوابط",
    })


def about(request):
    return render(request, 'about.html', {
        'pageTitle': " - درباره",
    })


def contact(request):
    return render(request, 'contact-us.html', {
        'pageTitle': " - تماس با ما",
    })
