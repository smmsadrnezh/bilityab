from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.core.context_processors import csrf
# Create your views here.


def login(request):
    invalid_html = ""

    if request.method == "POST":
        user = auth.authenticate(username=request.POST.get('signin-username', ''),
                                 password=request.POST.get('signin-password', ''))
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(request.REQUEST.get('next', ''))
        else:
            invalid_html = get_template('invalid.html').render()

    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', dict(c, **{'PageTitle': " - Login", 'invalid_html': invalid_html}))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def profile_edit(request, user_id):
    return render(request, 'profile.html', {

    })


def charge(request, user_id):
    return render(request, 'charge.html', {

    })


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')