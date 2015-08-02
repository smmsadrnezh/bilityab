from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

from account.models import CustomUser


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


def register(request):
    CustomUser.username = UserCreationForm.cleaned_data['signup-username']
    CustomUser.email = UserCreationForm.cleaned_data['signup-email']
    CustomUser.password = UserCreationForm.clean_password2()
    CustomUser.save()
    return HttpResponseRedirect('/login')


def profile_edit(request, user_id):
    return render(request, 'profile.html', {
        'logged_in': request.user.is_authenticated()

    })


def charge(request, user_id):
    return render(request, 'charge.html', {
        'logged_in': request.user.is_authenticated()

    })